# 四则运算题目生成器

## 项目概述

四则运算题目生成器是一个Python制作的图形用户界面(GUI)应用程序，旨在为小学生生成自定义的四则运算习题。该程序可以生成指定数量的题目，控制数值范围，并提供答案和评分功能。

## 功能特点

- 生成自定义数量的四则运算题目
- 控制题目中数值的范围
- 生成的题目包括加法、减法、乘法和除法
- 支持真分数的运算
- 自动生成题目答案
- 提供题目评分功能
- 直观的图形用户界面

## 安装说明

1. 确保您的系统已安装Python 3.6或更高版本。

2. 克隆或下载此仓库到本地机器。

3. 本项目主要依赖于Python的标准库，不需要安装额外的依赖包。

## 使用方法

1. 运行主程序：

   ```
   python main.py
   ```

2. 在打开的GUI窗口中：
   - 输入想要生成的题目数量
   - 输入题目中允许的最大数值
   - 点击"生成题目"按钮
   - 选择保存题目和答案文件的位置

3. 使用评分功能：
   - 点击"评分"按钮
   - 选择之前生成的题目文件和答案文件
   - 程序将生成评分报告

## 项目结构

```
FourOperationsProblemGenerator/
├── main/   # 核心代码包
│   ├── __init__.py
│   ├── expression.py     # 表达式类
│   ├── operation.py      # 算术运算类
│   ├── generator.py      # 生成算术题和答案的类
│   └── gui.py            # GUI 代码
├── tests/                # 测试代码包
│   ├── __init__.py
│   ├── test_arithmetic_problem_generator.py    # 对算术生成器的单元测试
│   ├── test_expression.py                      # 对算术表达式类的单元测试
│   ├── test_expression_generator.py            # 对单个表达式生成器的单元测试
│   └── test_operation.py                       # 对算术运算符类的单元测试
├── README.md             # 项目说明文档
├── setup.py              # 用于项目构建的配置文件
├── requirements.txt      # 依赖包列表
└── main.py               # 项目入口

```

## 核心类说明

- `Expression`：表示一个算术表达式
- `Operation`：表示一个算术运算，继承自`Expression`
- `ExpressionGenerator`：负责生成单个表达式
- `ArithmeticProblemGenerator`：管理整个题目生成过程
- `ArithmeticGUI`：创建和管理图形用户界面

## 注意事项

- 生成的题目不会产生负数
- 除法运算的结果总是真分数
- 每道题目中出现的运算符个数不超过3个
- 生成的题目不会重复

## 贡献

欢迎对本项目提出建议或贡献代码。请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 将您的更改推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 联系方式

如果您有任何问题或建议，请通过以下方式联系我们：

- 项目GitHub Issues页面
- 电子邮件：[您的邮箱地址]

感谢您使用四则运算题目生成器！