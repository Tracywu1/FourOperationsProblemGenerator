# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/20

import unittest
from fractions import Fraction
from main.expression import Expression
from main.operation import Operation
from main.generator import ExpressionGenerator, create_valid_operation


class TestExpressionGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ExpressionGenerator(10)

    def test_generate_number(self):
        # 测试数字生成
        for _ in range(100):  # 多次测试以确保正确性
            num = self.generator.generate_number()
            self.assertIsInstance(num, (int, Fraction))
            if isinstance(num, int):
                self.assertLess(num, 10)
            else:
                self.assertLess(num.numerator, 11)
                self.assertLess(num.denominator, 11)

    def test_generate_expression(self):
        # 测试表达式生成
        for _ in range(100):  # 多次测试以确保覆盖各种情况
            expr = self.generator.generate_expression()
            self.assertTrue(isinstance(expr, (Expression, Operation)))
            self.assertLessEqual(expr.operator_count, 3)

    def test_create_valid_operation(self):
        # 测试有效操作的创建
        left = Expression(5)
        right = Expression(3)
        op = create_valid_operation(left, right, '-')
        self.assertIsInstance(op, Operation)
        self.assertEqual(op.evaluate(), 2)

if __name__ == '__main__':
    unittest.main()