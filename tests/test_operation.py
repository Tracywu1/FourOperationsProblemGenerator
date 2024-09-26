# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/23

import unittest
from main.expression import Expression
from main.operation import Operation


class TestOperation(unittest.TestCase):
    def test_operation_init(self):
        # 测试Operation类的初始化
        left = Expression(5)
        right = Expression(3)
        op = Operation(left, right, '+')
        self.assertTrue(op.is_operation)
        self.assertEqual(op.operator_count, 1)

    def test_operation_str(self):
        # 测试Operation的字符串表示
        left = Expression(5)
        right = Expression(3)
        op = Operation(left, right, '+')
        self.assertEqual(str(op), "(5 + 3)")

    def test_operation_evaluate(self):
        # 测试Operation的evaluate方法
        left = Expression(5)
        right = Expression(3)
        op = Operation(left, right, '+')
        self.assertEqual(op.evaluate(), 8)

    def test_operation_to_string(self):
        # 测试Operation的to_string方法，包括复杂表达式
        a = Expression(1)
        b = Expression(2)
        c = Expression(3)
        op1 = Operation(a, b, '+')
        op2 = Operation(op1, c, '×')
        self.assertEqual(op2.to_string(), "(1 + 2) × 3")

    def test_invalid_operation(self):
        # 测试无效的Operation创建（如除以零）
        left = Expression(3)
        right = Expression(0)
        with self.assertRaises(ValueError):
            Operation(left, right, '÷')

if __name__ == '__main__':
    unittest.main()