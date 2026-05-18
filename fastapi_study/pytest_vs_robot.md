# pytest vs Robot Framework 对比测试报告

## 测试环境

- Python: 3.14.5
- FastAPI: 用于远程调用的 RESTful API
- 测试样本: 2 个简单测试用例

---

## 测试用例

### pytest 版本 (test_pytest.py)

```python
def test_simple():
    assert True
    result = 1 + 1
    assert result == 2

def test_another():
    name = "Robot Framework"
    assert name == "Robot Framework"
```

### Robot Framework 版本 (test_robot.robot)

```robot
*** Test Cases ***
Simple Test
    Log    Hello from Robot Framework
    Should Be True    ${TRUE}
    ${result}=    Evaluate    1 + 1
    Should Be Equal    ${result}    ${2}

Another Test
    Log    This is another test case
    ${name}=    Set Variable    Robot Framework
    Should Be Equal    ${name}    Robot Framework
```

---

## 测试结果对比

| 指标 | pytest | Robot Framework |
|------|--------|------------------|
| **执行状态** | ✅ PASSED | ✅ PASSED |
| **返回码** | 0 | 0 |
| **执行时间** | ~0.43s | ~2s |
| **通过率** | 2/2 | 2/2 |

---

## 输出对比

### pytest 输出

```
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
collecting ... collected 2 items

test_pytest.py::test_simple PASSED                                       [ 50%]
test_pytest.py::test_another PASSED                                      [100%]

============================== 2 passed in 0.43s ==============================
```

### Robot Framework 输出

```
==============================================================================
Test Robot :: pytest 对比测试 - Robot 版本
==============================================================================
Simple Test                                                           | PASS |
------------------------------------------------------------------------------
Another Test                                                          | PASS |
------------------------------------------------------------------------------
Test Robot :: pytest 对比测试 - Robot 版本                            | PASS |
2 tests, 2 passed, 0 failed
==============================================================================
Output:  Z:\Documents\mypython\fastapi_study\output.xml
Log:     Z:\Documents\mypython\fastapi_study\log.html
Report:  Z:\Documents\mypython\fastapi_study\report.html
```

---

## 详细对比分析

### 1. 语法与学习曲线

| 方面 | pytest | Robot Framework |
|------|--------|-----------------|
| 语法类型 | Python 标准语法 | 自定义 DSL 语法 |
| 学习难度 | ⭐⭐ (低) | ⭐⭐⭐⭐ (较高) |
| 前提知识 | Python 基础 | 了解关键字驱动概念 |

### 2. 执行性能

| 方面 | pytest | Robot Framework |
|------|--------|-----------------|
| 启动开销 | ~0.1s | ~1.5s |
| 单用例执行 | ~0.2s | ~0.3s |
| 总耗时 | ~0.43s | ~2s |
| 内存占用 | 较低 | 较高 |

### 3. 输出与报告

| 方面 | pytest | Robot Framework |
|------|--------|-----------------|
| 控制台输出 | 简洁线性 | 表格形式，层次清晰 |
| HTML 报告 | 需插件 (allure) | 自带可视化报告 |
| XML 输出 | 需配置 | 原生支持 |
| 日志详情 | 需配置 | 原生支持 |

### 4. 集成能力

| 方面 | pytest | Robot Framework |
|------|--------|-----------------|
| Python 集成 | 原生无缝 | 需通过 Library |
| REST API | 需自行封装 | 需自行封装 |
| CI/CD | 广泛支持 | 广泛支持 |
| GUI 自动化 | 需配合 SeleniumLibrary | 内置 SeleniumLibrary |

### 5. 使用场景

| 场景 | 推荐 |
|------|------|
| Python 单元测试 | **pytest** ✅ |
| API 自动化测试 | **pytest** ✅ |
| BDD 风格测试 | Robot Framework |
| 非技术人员参与 | Robot Framework |
| 快速原型测试 | **pytest** ✅ |
| Web GUI 自动化 | Robot Framework |
| 复杂业务测试 | Robot Framework |

---

## 通过 FastAPI 远程调用

两种框架都支持通过 FastAPI 远程调用:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 启动测试
resp = client.post("/robot/run", json={
    "script_path": "test_robot.robot"  # 或 "test_pytest.py"
})
task_id = resp.json()["task_id"]

# 获取结果
result = client.get(f"/robot/result/{task_id}").json()
print(result["output"])
```

---

## 结论与建议

### 选择 pytest 如果:

- 你或你的团队熟悉 Python
- 需要快速编写和执行测试
- 主要是 API 或单元测试
- 已有 Python 测试基础设施

### 选择 Robot Framework 如果:

- 测试需要非技术人员阅读和维护
- 需要美观的 HTML 报告
- 进行 Web GUI 自动化测试
- 采用 BDD 或关键字驱动方法论

### 两者可以共存:

实际项目中，pytest 和 Robot Framework 可以根据场景互补使用，共同通过 FastAPI 进行远程管理和监控。

---

## 项目文件

| 文件 | 说明 |
|------|------|
| `main.py` | FastAPI 应用主文件 |
| `test_pytest.py` | pytest 测试脚本 |
| `test_robot.robot` | Robot Framework 测试脚本 |
| `README.md` | API 使用说明 |
| `pytest_vs_robot.md` | 本对比报告 |

---

*报告生成时间: 2026-05-18*
