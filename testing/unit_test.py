# -*- coding:utf-8 -*-
from testing.module import Calculator
import unittest

class ModuleTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(8,4)
    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result,12)
    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result,4)
    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result,32)
    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result,2)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(ModuleTest('test_add'))
    # suite.addTest(ModuleTest('test_sub'))
    # suite.addTest(ModuleTest('test_mul'))
    # suite.addTest(ModuleTest('test_div'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #pull一下看看什么情况