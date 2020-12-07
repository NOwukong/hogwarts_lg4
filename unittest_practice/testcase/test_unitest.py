# -*- coding: utf-8 -*-
# @Time     :2020/12/5 13:48
# @Author   :xiangdong
# @File     :test_unitest.py

import unittest


class TestDemo(unittest.TestCase):
    # setUp 方法是在每个测试案例def方法前执行一遍
    def setUp(self) -> None:
        print("开始")

    # tearDown 方法是在每个测试案例def方法后执行一遍
    def tearDown(self) -> None:
        print('结束')

    # setupClass 方法是在整个类前执行一遍
    @classmethod
    def setUpClass(cls) -> None:
        print('set Up Class')

    # tearDownClass 方法是在整个类后执行一遍
    @classmethod
    def tearDownClass(cls) -> None:
        print('tear Down Class')

    def test_abc(self):
        print("test_abc")

    def test_upper(self):
        print('test_upper 111')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test_isupper 222')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        print('test_split 333')
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
