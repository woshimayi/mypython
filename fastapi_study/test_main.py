"""
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited.
@contact: woshidamayi@gmail.com
@software: dof
@file: test_main.py
@time: 2026/5/18
@desc: Robot Framework API 测试
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Robot Framework API", "version": "1.0.0"}


def test_list_tasks():
    response = client.get("/robot/tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()


def test_get_status_not_found():
    response = client.get("/robot/status/nonexistent")
    assert response.status_code == 404


def test_get_result_not_found():
    response = client.get("/robot/result/nonexistent")
    assert response.status_code == 404


def test_cancel_not_found():
    response = client.delete("/robot/cancel/nonexistent")
    assert response.status_code == 404


def test_run_script_not_found():
    response = client.post("/robot/run", json={"script_path": "/nonexistent.robot"})
    assert response.status_code == 404
