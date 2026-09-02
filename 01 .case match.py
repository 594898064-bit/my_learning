# # 模式匹配match...case
# # 复习一下就是f{结构}
# # 这个结构是将int 等类型的函数转换为字符串
# # 例如就是
# a = 13
# b = 12
# print(f"{a}+{b}={a+b}")
# # # 1 .插入变量
# name = "Bob"
# score = 95
# print(f"学生: {name}, 分数: {score}")
# # 输出: 学生: Bob, 分数: 95
#
# # 2 .表达式计算
# a = 10
# b = 20
# print(f"{a} + {b} = {a + b}")
# print(f"{a} × {b} = {a * b}")
# # 输出: 10 + 20 = 30
# #      10 × 20 = 200
#
# # 3 .格式化数字
# price = 123.456789
# print(f"价格: {price:.2f}")  # 保留2位小数
# # 输出: 价格: 123.46
#
# num = 1000000
# print(f"数字: {num:,}")  # 千位分隔符
# # 输出: 数字: 1,000,000
#

# match....case函数
# day = input("请输入今天是星期几:")
# match day:
#     case "1"|"一":
#         print("今天星期一")
#     case"2"| "二":
#         print("今天星期二")
#     case"3"|"三":
#         print("今天星期三")
#     case _ :
#         print("输入有误")


# 例二:
# 简易计算器
num1 = float(input("请输入第一个数字:"))
num2 = float(input("请输入第二个数字"))
opera = input("请输入计算符(+ - * /)")
match opera:
    case "+":
        print(f"{num1} +{num2} = {num1+num2}")
    case "-":
        print(f"{num1} -{num2} = {num1-num2}")
    case "*":
        print(f"{num1} *{num2} = {num1*num2}")
    case "/"    if num2!= 0:
        print(f"{num1} / {num2} = {num1/num2}")
    case _ :
        print("无效符号")