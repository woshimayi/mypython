"""
pytest 版本测试脚本 - 与 demo.robot 等效的测试用例
"""

def test_simple():
    """简单测试"""
    assert True
    result = 1 + 1
    assert result == 2

def test_another():
    """另一个测试"""
    name = "Robot Framework"
    assert name == "Robot Framework"
