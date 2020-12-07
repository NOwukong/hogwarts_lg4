# -*- coding: utf-8 -*-
# @Time     :2020/12/5 14:13
# @Author   :xiangdong
# @File     :test_search.py

import unittest


class Search():

    def search_fun(self):
        print('search')
        return True


class TestSearch1(unittest.TestCase):

    # @classmethod
    # # 用setup方法可以实现每个测试案例方法前执行一遍实例化对象
    # def setUpClass(cls) -> None:
    #     # 实例化一个父类对象，可以免去下面每个测试案例方法都实例化一次对象
    #     cls.search = Search()
    #     print('setup class')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('tearDown Class')

    # 每次执行下面的案例前执行一次
    def setUp(self) -> None:
        self.search = Search()
        print('set up -----方法级')

    # 每次执行下面的案例后执行一次
    def tearDown(self) -> None:
        print('tear down -----方法级')

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 2, '判断 1==1')

    def test_notequal(self):
        print("断言不相等")
        # self.assertNotEqual(1, 1, '判断 1!=2')
        self.assertTrue(1 == 2, 'verify')


class TestSearch2(unittest.TestCase):
    # 每次执行下面的案例前执行一次
    def setUp(self) -> None:
        self.search = Search()
        print('set up >>>>> 方法级')

    # 每次执行下面的案例后执行一次
    def tearDown(self) -> None:
        print('tear down >>>>> 方法级')

    def test_case1(self):
        print("testcase1")


if __name__ == '__main__':
    # 方法一：执行当前当前文件下所有的unittest测试用例
    # unittest.main()

    # 方法二：执行只指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
    # 创建一个测试套件，TestSuit
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch1('test_search1'))
    # suite.addTest(TestSearch1('test_search3'))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)