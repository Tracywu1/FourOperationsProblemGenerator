# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/23

import unittest
from fractions import Fraction
from main.generator import ArithmeticProblemGenerator


class TestArithmeticProblemGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ArithmeticProblemGenerator(10, 10)

    def test_generate_problems(self):
        # 测试问题生成
        self.generator.generate_problems()
        self.assertEqual(len(self.generator.problems), 10)
        for problem in self.generator.problems:
            self.assertIn('=', problem)

    def test_evaluate_expression(self):
        # 测试表达式评估
        result = self.generator.evaluate_expression("2 + 3 × 4")
        self.assertEqual(result, 14)

    def test_format_result(self):
        # 测试结果格式化
        self.assertEqual(self.generator.format_result(Fraction(1, 2)), "1/2")
        self.assertEqual(self.generator.format_result(3.5), "3.5")
        self.assertEqual(self.generator.format_result(4), "4")


if __name__ == '__main__':
    unittest.main()
