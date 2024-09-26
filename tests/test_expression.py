# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/23

import unittest
from main.expression import Expression


class TestExpression(unittest.TestCase):
    def test_expression_init(self):
        # 测试Expression类的初始化
        expr = Expression(5)
        self.assertEqual(expr.value, 5)
        self.assertFalse(expr.is_operation)
        self.assertEqual(expr.operator_count, 0)

    def test_expression_str(self):
        # 测试Expression的字符串表示
        expr = Expression(5)
        self.assertEqual(str(expr), "5")

    def test_expression_evaluate(self):
        # 测试Expression的evaluate方法
        expr = Expression(5)
        self.assertEqual(expr.evaluate(), 5)

if __name__ == '__main__':
    unittest.main()