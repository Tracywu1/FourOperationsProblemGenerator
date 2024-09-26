# setup.py

from setuptools import setup, find_packages

setup(
    name='arithmetic_problem_generator',  # 项目名称
    version='0.1.0',  # 项目版本
    description='A Python package for generating and grading four operations problems with a GUI interface.',
    author='Tracy Wu',  # 作者
    author_email='tracywu0409@gmail.com',  # 作者邮箱
    packages=find_packages(),  # 自动查找项目中的所有包
    install_requires=[  # 项目依赖
        'tkinter',      # GUI 库
        'fractions',    # 分数运算
        'decimal',      # 高精度小数运算
    ],
    entry_points={
        'console_scripts': [
            'arithmetic-gui=arithmetic_problem.gui:main',  # 在命令行中使用 `arithmetic-gui` 启动 GUI
        ],
    },
)