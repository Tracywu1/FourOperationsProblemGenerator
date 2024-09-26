# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/20
from fractions import Fraction

from main.expression import Expression


class Operation(Expression):
    """
    表示一个算术运算。
    这是Expression的子类，用于处理两个表达式之间的运算。
    """

    def __init__(self, left, right, operator):
        """
        初始化算术运算。
        :param left: 左侧表达式。
        :param right: 右侧表达式。
        :param operator: 运算符（+，-，×，÷）。
        """
        super().__init__(None)
        self.left = left
        self.right = right
        self.operator = operator
        self.is_operation = True
        self.operator_count = left.operator_count + right.operator_count + 1

        # 在初始化时进行约束检查
        if not self.is_valid_operation():
            raise ValueError("Invalid operation")

    def is_valid_operation(self):
        # 检查总运算符数量
        if self.operator_count > 3:
            return False

        # 检查减法操作，确保不会产生负数
        if self.operator == '-' and self.left.evaluate() < self.right.evaluate():
            return False

        # 检查除法操作
        if self.operator == '÷':
            right_value = self.right.evaluate()
            # 确保除数不为零
            if right_value == 0:
                return False
            # 确保结果为真分数（如果是分数的话）
            if isinstance(right_value, Fraction) and self.left.evaluate() <= right_value:
                return False

        # 避免生成 1 × x、x × 1 或 x ÷ 1 这样的表达式
        if (self.operator == '×' and (self.left.evaluate() == 1 or self.right.evaluate() == 1)) or \
                (self.operator == '÷' and self.right.evaluate() == 1):
            return False

        return True

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

    def evaluate(self):
        """
        根据运算符和操作数计算运算结果。
        :return: 运算结果。
        """
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        if self.operator == '+':
            return left_val + right_val
        elif self.operator == '-':
            return left_val - right_val
        elif self.operator == '×':
            return left_val * right_val
        elif self.operator == '÷':
            return left_val / right_val

    def to_string(self):
        # Implement proper parentheses handling
        left_str = self.left.to_string() if isinstance(self.left, Operation) and self.left.operator in ['+',
                                                                                                        '-'] else str(
            self.left)
        right_str = self.right.to_string() if isinstance(self.right, Operation) and self.right.operator in ['+',
                                                                                                            '-'] else str(
            self.right)

        if self.operator in ['×', '÷']:
            if isinstance(self.left, Operation) and self.left.operator in ['+', '-']:
                left_str = f"({left_str})"
            if isinstance(self.right, Operation) and self.right.operator in ['+', '-']:
                right_str = f"({right_str})"

        return f"{left_str} {self.operator} {right_str}"
