# -*- coding: utf-8 -*-
# @Time     :2020/12/7 21:28
# @Author   :xiangdong
# @File     :run.py

import unittest

from hogwarts_lg4.util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    report_title = '我的 demo 测试用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'D:/python_learn/hogwarts_lg4/unittest_practice/result.html'

    test_dir = 'D:/python_learn/hogwarts_lg4/unittest_practice/testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)