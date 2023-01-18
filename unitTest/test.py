import unittest
from m1 import MyClass


"""
unittest框架中4个重要的概念：

test fixture:是初始化和清理测试数据及环境，通过重写TestCase的setUp()和tearDown()方法来实现
test case:是测试用例
test suite:是测试用例的集合（俗称测试套件），通过addTest加载TestCase到TestSuite中，返回一个TestSuite实例。
test runner:的作用是运行测试用例并返回结果，通过TextTestRunner类提供的run()方法来执行test suite或test case。
"""


class MyClassTest(unittest.TestCase):
    def setUp(self):
        self.calc = MyClass(7, 5)

    def tearDown(self):
        pass

    def test_add(self):
        ret = self.calc.add()
        self.assertEqual(ret, 12)

    def test_sub(self):
        ret = self.calc.sub()
        self.assertEqual(ret, 2)


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(MyClassTest('test_add'))
    suite.addTest(MyClassTest('test_sub'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
