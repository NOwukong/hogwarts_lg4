# -*- coding: utf-8 -*-
# @Time     :2020/12/14 21:01
# @Author   :xiangdong
# @File     :pytest_demo.py
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_a():
    assert func(3) == 4

def test_b():
    assert func(5) == 6

if __name__ == '__main__':
    pytest.main(['pytest_demo.py'])