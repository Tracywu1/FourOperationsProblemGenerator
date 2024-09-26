# -*- coding: utf-8 -*-
# Author: Lenovo
# Created on: 2024/9/20
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from main.generator import ArithmeticProblemGenerator


class ArithmeticGUI:
    """
    用于生成算术题目和评分答案的图形用户界面。
    """

    def __init__(self, master):
        """
        初始化图形用户界面。
        :param master: tkinter的主窗口。
        """
        self.generator = None
        self.master = master
        master.title("算术题目生成器")
        master.geometry("400x300")

        # 创建并放置控件
        ttk.Label(master, text="题目数量:").grid(row=0, column=0, padx=5, pady=5)
        self.num_problems = ttk.Entry(master)
        self.num_problems.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(master, text="最大值范围:").grid(row=1, column=0, padx=5, pady=5)
        self.max_value = ttk.Entry(master)
        self.max_value.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(master, text="生成题目", command=self.generate_problems).grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(master, text="评分", command=self.grade_problems).grid(row=3, column=0, columnspan=2, pady=10)

        self.status = ttk.Label(master, text="")
        self.status.grid(row=4, column=0, columnspan=2, pady=10)

        # 进度条
        self.progress = ttk.Progressbar(master, length=200, mode='determinate')
        self.progress.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_problems(self):
        """
        在后台线程中生成题目，并更新进度条。
        """
        try:
            num_problems = int(self.num_problems.get())
            max_value = int(self.max_value.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数")
            return

        self.generator = ArithmeticProblemGenerator(num_problems, max_value)
        self.progress['maximum'] = num_problems

        def generate():
            self.generator.generate_problems()
            self.generator.save_problems()
            self.generator.save_answers()
            self.master.after(0, self.finish_generation)

        def update_progress():
            current = len(self.generator.problems)
            self.progress['value'] = current
            self.status.config(text=f"已生成 {current} 道题目")
            if current < num_problems:
                self.master.after(100, update_progress)

        threading.Thread(target=generate, daemon=True).start()
        update_progress()

    def finish_generation(self):
        """
        完成题目生成后的操作。
        """
        try:
            self.status.config(text=f"题目生成完成! 总共生成 {len(self.generator.problems)} 道题目")
        except Exception as e:
            self.status.config(text=f"生成过程中出错: {str(e)}")
        finally:
            self.progress['value'] = 0

    def grade_problems(self):
        """
        通过比较用户答案与计算答案来评分题目。
        """
        answer_file = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")], title="选择答案文件")

        if not answer_file:
            return

        correct, wrong = self.check_answers('Exercises.txt', answer_file)

        with open('Grade.txt', 'w') as f:
            f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
            f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")

        self.status.config(text="评分完成!")

    def check_answers(self, exercise_file, answer_file):
        """
        通过比较计算结果与提供的答案来检查答案。
        :param exercise_file: 题目文件路径。
        :param answer_file: 答案文件路径。
        :return: 正确和错误答案的题号列表。
        """
        correct = []
        wrong = []
        generator = ArithmeticProblemGenerator(1, 1)  # 仅用于使用其方法
        with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
            for i, (exercise, answer) in enumerate(zip(ef, af), 1):
                exercise = exercise.split('.', 1)[1].strip()
                answer = answer.split('.', 1)[1].strip()

                calculated_answer = generator.evaluate_expression(exercise.split('=')[0].strip())
                formatted_calculated = generator.format_result(calculated_answer)
                if self.compare_answers(formatted_calculated, answer):
                    correct.append(i)
                else:
                    wrong.append(i)
        return correct, wrong

    def compare_answers(self, calculated, provided):
        """
        比较计算答案与提供的答案。
        :param calculated: 计算得出的答案。
        :param provided: 提供的答案。
        :return: 如果答案匹配则返回True，否则返回False。
        """
        # 移除所有空白字符并转换为小写以进行比较
        calculated = ''.join(calculated.split()).lower()
        provided = ''.join(provided.split()).lower()
        return calculated == provided


def main():
    root = tk.Tk()
    app = ArithmeticGUI(root)
    root.mainloop()
