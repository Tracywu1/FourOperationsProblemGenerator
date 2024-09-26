# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/20

class Expression:
    """
    表示一个算术表达式。
    可以是单个值或复杂的运算。
    """

    def __init__(self, value):
        """
        初始化表达式。
        :param value: 表达式的值。
        """
        self.value = value
        self.is_operation = False  # 表示该表达式是否是一个运算
        self.operator_count = 0

    def __str__(self):
        """
        返回表达式的字符串表示形式。
        :return: 表达式的字符串形式。
        """
        return str(self.value)

    def evaluate(self):
        """
        计算表达式的值。
        :return: 表达式的值。
        """
        return self.value

    def to_string(self):
        return str(self)
