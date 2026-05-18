# Robot Framework RESTful API

远程调用 Robot 测试脚本的 RESTful 接口，支持 POST/GET 和 WebSocket。

## 快速开始

```bash
pip install robotframework fastapi uvicorn
uvicorn main:app --reload --port 8002
```

访问 http://127.0.0.1:8002/docs 查看交互式 API 文档。

## API 接口

### 1. 启动测试任务

```bash
POST /robot/run
```

**请求体：**
```json
{
  "script_path": "demo.robot",
  "args": ["--exclude", "slow"]
}
```

**响应：**
```json
{
  "task_id": "a1b2c3d4",
  "message": "测试任务已启动"
}
```

### 2. 获取任务状态

```bash
GET /robot/status/{task_id}
```

**响应：**
```json
{
  "task_id": "a1b2c3d4",
  "status": "completed",
  "start_time": "2026-05-18T10:30:00",
  "end_time": "2026-05-18T10:30:05",
  "output": "==============================================================================\nDemo :: Demo test suite..."
}
```

### 3. 获取测试结果

```bash
GET /robot/result/{task_id}
```

**响应：**
```json
{
  "task_id": "a1b2c3d4",
  "status": "completed",
  "return_code": 0,
  "output": "2 tests, 2 passed, 0 failed",
  "error": "",
  "result_file": "Z:\\path\\to\\output.xml"
}
```

### 4. 列出所有任务

```bash
GET /robot/tasks
```

### 5. 取消任务

```bash
DELETE /robot/cancel/{task_id}
```

### 6. WebSocket 实时推送

```bash
WS /ws/robot/{task_id}
```

**客户端发送：**
- `ping` - 心跳检测
- `status` - 获取当前状态

**服务端推送：**
```json
{"type": "connected", "task_id": "a1b2c3d4", "status": "running"}
{"type": "output", "line": "Simple Test                                                           | PASS |"}
{"type": "status", "status": "completed", "message": "测试执行成功", "return_code": 0}
{"type": "result_file", "path": "Z:\\path\\to\\output.xml"}
{"type": "log_file", "path": "Z:\\path\\to\\log.html"}
{"type": "report_file", "path": "Z:\\path\\to\\report.html"}
```

## 状态值

| 状态 | 说明 |
|------|------|
| `pending` | 任务等待中 |
| `running` | 任务执行中 |
| `completed` | 任务成功完成 |
| `failed` | 任务执行失败 |
| `cancelled` | 任务已取消 |

## 使用示例

### Python 调用

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 启动任务
resp = client.post("/robot/run", json={"script_path": "tests/demo.robot"})
task_id = resp.json()["task_id"]

# 查询状态
status = client.get(f"/robot/status/{task_id}")
print(status.json())
```

### WebSocket 客户端

```python
import websockets
import asyncio

async def main():
    async with websockets.connect("ws://localhost:8002/ws/robot/a1b2c3d4") as ws:
        # 接收实时消息
        async for message in ws:
            data = json.loads(message)
            print(data)

asyncio.run(main())
```

## 项目结构

```
.
├── main.py      # FastAPI 应用主文件
├── test_main.py # 单元测试
├── demo.robot   # 示例测试脚本
└── README.md    # 本文档
```
