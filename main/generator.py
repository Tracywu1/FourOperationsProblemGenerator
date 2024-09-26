# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/20
import itertools
import random

from collections import Counter
from fractions import Fraction
from _decimal import Decimal

from main.expression import Expression
from main.operation import Operation


def create_valid_operation(left, right, operator):
    """
    创建有效的运算，避免问题案例。
    :param left: 左操作数。
    :param right: 右操作数。
    :param operator: 运算符。
    :return: 有效的运算表达式。
    """
    try:
        return Operation(left, right, operator)
    except ValueError:
        # 如果操作无效，返回一个有效的单一操作数
        return left if left.operator_count >= right.operator_count else right


class ExpressionGenerator:
    """
    根据给定参数生成算术表达式。
    """

    def __init__(self, max_value):
        """
        初始化表达式生成器。
        :param max_value: 生成数字的最大值。
        """
        self.max_value = max_value

    def generate_number(self):
        """
        生成一个随机数或分数。
        :return: 随机生成的数或分数。
        """
        if random.choice([True, False]):
            # 生成随机分数
            return Fraction(random.randint(1, self.max_value), random.randint(1, self.max_value))
        else:
            # 生成随机整数
            return random.randint(0, self.max_value - 1)

    def generate_expression(self, max_operators=3):
        """
        递归生成表达式。
        通过调整概率来增加生成复杂表达式的机会。
        :param max_operators: 最大运算符数
        :return: 生成的表达式。
        """
        if max_operators == 0 or random.random() < 0.3:  # 70% 的机会生成复杂表达式
            return Expression(self.generate_number())

        left = self.generate_expression(max_operators - 1)
        right = self.generate_expression(max_operators - 1)
        operator = random.choice(['+', '-', '×', '÷'])

        try:
            return Operation(left, right, operator)
        except ValueError:
            # 如果操作无效，返回左操作数或右操作数
            return left if random.choice([True, False]) else right


def interleave(numbers, operators):
    result = [numbers[0]]
    for num, op in zip(numbers[1:], operators):
        result.extend([op, num])
    return ' '.join(result) + ' = '


class ArithmeticProblemGenerator:
    """
    根据给定参数生成算术题目。
    """

    def __init__(self, num_problems, max_value):
        """
        初始化算术题目生成器。
        :param num_problems: 要生成的题目数量。
        :param max_value: 生成数字的最大值。
        """
        self.num_problems = num_problems
        self.max_value = max_value
        self.expression_generator = ExpressionGenerator(max_value)
        self.problems = set()
        self.problem_signatures = Counter()  # 用于存储问题签名
        self.normalized_problems = set()

    def generate_problems(self):
        """
        生成指定数量的不重复题目。
        使用问题签名来提高效率，并增加重试次数。
        """
        attempts = 0
        max_attempts = self.num_problems * 100  # 设置最大尝试次数

        while len(self.problems) < self.num_problems and attempts < max_attempts:
            expression = self.expression_generator.generate_expression()
            if not isinstance(expression, Operation):
                continue  # 跳过不包含运算符的表达式

            problem = f"{expression.to_string()} = "
            signature = self.get_problem_signature(expression)

            # 首先检查签名
            if self.problem_signatures[signature] == 0:
                # 如果签名是新的，再检查规范化表达式
                normalized = self.normalize_expression(problem)
                if normalized not in self.normalized_problems:
                    self.problems.add(problem)
                    self.problem_signatures[signature] += 1
                    self.normalized_problems.add(normalized)
            attempts += 1

        if len(self.problems) < self.num_problems:
            print(f"警告：只能生成 {len(self.problems)} 道不重复的题目。")

    def get_problem_signature(self, expression):
        """
        生成问题的唯一签名，考虑操作数和运算符。
        """
        if isinstance(expression, Expression) and not isinstance(expression, Operation):
            return str(expression.value)
        elif isinstance(expression, Operation):
            left_sig = self.get_problem_signature(expression.left)
            right_sig = self.get_problem_signature(expression.right)
            return f"({left_sig}{expression.operator}{right_sig})"

    def normalize_expression(self, problem):
        expr = problem.split('=')[0].strip()
        tokens = expr.replace('(', '').replace(')', '').split()
        numbers = [token for token in tokens if token not in ['+', '-', '×', '÷']]
        operators = [token for token in tokens if token in ['+', '-', '×', '÷']]

        # 对可交换的运算符（+和×）进行排序
        sorted_parts = []
        current_part = [numbers[0]]
        for num, op in zip(numbers[1:], operators):
            if op in ['+', '×']:
                current_part.append(num)
            else:
                sorted_parts.append((''.join(sorted(current_part)), op))
                current_part = [num]
        sorted_parts.append(''.join(sorted(current_part)))

        # 将排序后的部分重新组合
        return ' '.join(f"{part[0]}{part[1]}" if isinstance(part, tuple) else part for part in sorted_parts)

    def save_problems(self):
        """
        将生成的题目保存到文件。
        """
        with open('Exercises.txt', 'w') as f:
            for i, problem in enumerate(self.problems, 1):
                f.write(f"{i}. {problem}\n")

    def save_answers(self):
        """
        计算并保存答案到文件。
        """
        with open('Answers.txt', 'w') as f:
            for i, problem in enumerate(self.problems, 1):
                expression = problem.split('=')[0].strip()
                answer = self.evaluate_expression(expression)
                f.write(f"{i}. {self.format_result(answer)}\n")

    def evaluate_expression(self, expression):
        """
        计算表达式并返回结果。
        :param expression: 要计算的表达式。
        :return: 表达式的计算结果。
        """
        # 使用 Decimal 进行精确计算
        return eval(expression.replace('×', '*').replace('÷', '/'), {'Fraction': Fraction, 'Decimal': Decimal})

    def format_result(self, value):
        """
        格式化结果，处理精度问题。
        :param value: 要格式化的值。
        :return: 格式化后的结果字符串。
        """
        if isinstance(value, Fraction):
            # 对于分数，我们保持原样
            if value.denominator == 1:
                return str(value.numerator)
            whole = value.numerator // value.denominator
            if whole:
                remainder = value - whole
                return f"{whole}'{remainder.numerator}/{remainder.denominator}"
            return f"{value.numerator}/{value.denominator}"
        elif isinstance(value, (int, Decimal)):
            # 对于整数和小数，我们使用 Decimal 来控制精度
            return str(Decimal(value).normalize())
        else:
            # 对于其他类型，我们转换为 Decimal 并格式化
            return str(Decimal(str(value)).normalize())
