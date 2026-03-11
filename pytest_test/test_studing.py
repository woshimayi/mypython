'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: test_studing.py
@time: 2025/01/14 14:27
@desc: 
'''


import pytest

# @pytest.mark.model
# def test_model_a():
#     print("\033[0;31;40m 执行test_model_a \033[0m")
#
# @pytest.mark.regular
# def test_regular_a():
#     print("\033[0;31;40m test_regular_a \033[0m")
#
# @pytest.mark.model
# def test_model_b():
#     print("\033[0;31;40m test_model_b \033[0m")
#
# @pytest.mark.regular
# class TestClass:
#     def test_method(self):
#         print("\033[0;31;40m test_method \033[0m")
#
# def testnoMark():
#     print("testnoMark")
#
# if __name__ == '__main__':
#     print('Hello world')


# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClass:   #请确保你的类以 Test 为前缀
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "hello")
