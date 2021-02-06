# -*- coding: utf-8 -*-
# @Time     :2020/12/26 16:49
# @Author   :xiangdong
# @File     :allure_demo.py

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')
