"""
@author: dof
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited.
@contact: woshidamayi@gmail.com
@software: dof
@file: main.py
@time: 2026/5/18
@desc: Robot Framework RESTful API - 支持 POST/GET/WebSocket 远程调用 Robot 测试脚本
"""

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, Path
from pydantic import BaseModel
from typing import Optional
import subprocess
import uuid
import json
import os
import asyncio
from datetime import datetime
from enum import Enum
from collections import defaultdict

app = FastAPI(
    title="Robot Framework API",
    description="远程调用 Robot 测试脚本的 RESTful API",
    version="1.0.0",
)


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RobotTestTask:
    def __init__(self, task_id: str, script_path: str, args: Optional[list] = None):
        self.task_id = task_id
        self.script_path = script_path
        self.args = args or []
        self.status = TaskStatus.PENDING
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.output: str = ""
        self.error: str = ""
        self.return_code: Optional[int] = None
        self.result_file: Optional[str] = None
        self._process: Optional[subprocess.Popen] = None
        self._websocket_connections: list[WebSocket] = []

    def add_websocket(self, ws: WebSocket):
        self._websocket_connections.append(ws)

    def remove_websocket(self, ws: WebSocket):
        if ws in self._websocket_connections:
            self._websocket_connections.remove(ws)

    async def broadcast(self, message: dict):
        disconnected = []
        for ws in self._websocket_connections:
            try:
                await ws.send_json(message)
            except Exception:
                disconnected.append(ws)
        for ws in disconnected:
            self.remove_websocket(ws)

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "script_path": self.script_path,
            "args": self.args,
            "status": self.status.value,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "output": self.output,
            "error": self.error,
            "return_code": self.return_code,
            "result_file": self.result_file,
        }


task_store: dict[str, RobotTestTask] = {}


class RunRequest(BaseModel):
    script_path: str
    args: Optional[list[str]] = None


class RunResponse(BaseModel):
    task_id: str
    message: str


class StatusResponse(BaseModel):
    task_id: str
    status: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    output: str = ""


class ResultResponse(BaseModel):
    task_id: str
    status: str
    return_code: Optional[int]
    output: str
    error: str
    result_file: Optional[str]


@app.post("/robot/run", response_model=RunResponse, tags=["Robot"])
async def run_robot_test(request: RunRequest):
    """
    启动 Robot 测试脚本
    - **script_path**: Robot 测试脚本 (.robot) 的路径
    - **args**: 可选的 Robot 命令行参数
    """
    if not os.path.exists(request.script_path):
        raise HTTPException(status_code=404, detail=f"脚本文件不存在: {request.script_path}")

    task_id = str(uuid.uuid4())[:8]
    task = RobotTestTask(task_id, request.script_path, request.args)
    task_store[task_id] = task

    asyncio.create_task(_run_test_task(task_id))

    return RunResponse(task_id=task_id, message="测试任务已启动")


async def _run_test_task(task_id: str):
    """异步执行测试任务"""
    task = task_store.get(task_id)
    if not task:
        return

    task.status = TaskStatus.RUNNING
    task.start_time = datetime.now()
    await task.broadcast({"type": "status", "status": "running", "message": "测试开始执行"})

    try:
        import sys
        script_ext = os.path.splitext(task.script_path)[1].lower()

        if script_ext == ".robot":
            script_dir = os.path.dirname(os.path.abspath(task.script_path))
            cmd = [sys.executable, "-m", "robot", "--outputdir", script_dir, task.script_path] + task.args
        elif script_ext == ".py":
            script_dir = os.path.dirname(os.path.abspath(task.script_path)) or "."
            cmd = [sys.executable, "-m", "pytest", task.script_path, "-v", "--tb=short"] + task.args
        else:
            raise ValueError(f"不支持的脚本类型: {script_ext}")

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        task._process = process

        for line in iter(process.stdout.readline, ""):
            if line:
                task.output += line
                await task.broadcast({"type": "output", "line": line.rstrip()})

        process.wait()
        task.return_code = process.returncode
        task.end_time = datetime.now()

        if task.return_code == 0:
            task.status = TaskStatus.COMPLETED
            await task.broadcast({
                "type": "status",
                "status": "completed",
                "message": "测试执行成功",
                "return_code": 0
            })
        else:
            task.status = TaskStatus.FAILED
            await task.broadcast({
                "type": "status",
                "status": "failed",
                "message": f"测试执行失败 (返回码: {task.return_code})",
                "return_code": task.return_code
            })

        stderr = process.stderr.read()
        if stderr:
            task.error = stderr
            await task.broadcast({"type": "error", "message": stderr})

        if script_ext == ".robot":
            import re
            output_match = re.search(r'Output:\s+(.+)', task.output)
            log_match = re.search(r'Log:\s+(.+)', task.output)
            report_match = re.search(r'Report:\s+(.+)', task.output)
            if output_match:
                task.result_file = output_match.group(1).strip()
                await task.broadcast({"type": "result_file", "path": task.result_file})
            if log_match:
                await task.broadcast({"type": "log_file", "path": log_match.group(1).strip()})
            if report_match:
                await task.broadcast({"type": "report_file", "path": report_match.group(1).strip()})

    except Exception as e:
        task.status = TaskStatus.FAILED
        task.error = str(e)
        task.end_time = datetime.now()
        await task.broadcast({"type": "error", "status": "failed", "message": str(e)})


@app.get("/robot/status/{task_id}", response_model=StatusResponse, tags=["Robot"])
async def get_task_status(task_id: str = Path(description="任务 ID")):
    """获取任务执行状态"""
    task = task_store.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"任务不存在: {task_id}")

    return StatusResponse(
        task_id=task.task_id,
        status=task.status.value,
        start_time=task.start_time.isoformat() if task.start_time else None,
        end_time=task.end_time.isoformat() if task.end_time else None,
        output=task.output
    )


@app.get("/robot/result/{task_id}", response_model=ResultResponse, tags=["Robot"])
async def get_task_result(task_id: str = Path(description="任务 ID")):
    """获取任务测试结果"""
    task = task_store.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"任务不存在: {task_id}")

    if task.status == TaskStatus.RUNNING:
        raise HTTPException(status_code=202, detail="任务仍在执行中")
    if task.status == TaskStatus.PENDING:
        raise HTTPException(status_code=202, detail="任务尚未开始执行")

    return ResultResponse(
        task_id=task.task_id,
        status=task.status.value,
        return_code=task.return_code,
        output=task.output,
        error=task.error,
        result_file=task.result_file
    )


@app.get("/robot/tasks", tags=["Robot"])
async def list_tasks():
    """列出所有任务"""
    return {"tasks": [task.to_dict() for task in task_store.values()]}


@app.delete("/robot/cancel/{task_id}", tags=["Robot"])
async def cancel_task(task_id: str = Path(description="任务 ID")):
    """取消正在执行的任务"""
    task = task_store.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"任务不存在: {task_id}")

    if task.status != TaskStatus.RUNNING:
        raise HTTPException(status_code=400, detail=f"任务当前状态为 {task.status.value}，无法取消")

    if task._process:
        task._process.terminate()
        task.status = TaskStatus.CANCELLED
        task.end_time = datetime.now()
        return {"message": "任务已取消", "task_id": task_id}

    raise HTTPException(status_code=500, detail="任务进程不存在")


@app.websocket("/ws/robot/{task_id}")
async def websocket_robot(websocket: WebSocket, task_id: str):
    """WebSocket 实时接收任务执行进度"""
    task = task_store.get(task_id)
    if not task:
        await websocket.accept()
        await websocket.send_json({"type": "error", "message": f"任务不存在: {task_id}"})
        await websocket.close(code=4004)
        return

    await websocket.accept()
    task.add_websocket(websocket)

    try:
        await websocket.send_json({
            "type": "connected",
            "task_id": task_id,
            "status": task.status.value
        })

        if task.status == TaskStatus.COMPLETED:
            await websocket.send_json({"type": "status", "status": "completed", "message": "任务已完成"})
        elif task.status == TaskStatus.FAILED:
            await websocket.send_json({"type": "status", "status": "failed", "message": "任务失败"})
        elif task.status == TaskStatus.RUNNING:
            await websocket.send_json({"type": "status", "status": "running", "message": "任务执行中"})

        while True:
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_json({"type": "pong"})
            elif data == "status":
                await websocket.send_json({"type": "status", "status": task.status.value})

    except WebSocketDisconnect:
        task.remove_websocket(websocket)


@app.get("/", tags=["默认"])
async def root():
    return {"message": "Robot Framework API", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
