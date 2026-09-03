# 输入用户名的密码执行操作,具体要求如下
# 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
# 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# 输入的用户名和密码不能为空
# 登录成功：输出“登录成功，进入B站首页~”
# 登录失败：输出“用户名或密码错误，请重新输入！”


# 关键字:
# break :只能够出现在循环中,表示结束跳出循环的含义
# continue:也只能出现在循环中,表示中断本次循环直接进入下一个循环当中.
while True:
        # 接受输入的用户名和密码
    user= input("请输入您的用户名:")
    password= input("请输入您的密码:")

    if user== " " or  password== " ":
        print("输入的密码或账户不能为空")
        continue
    elif user== "zengxu"and password == "666888":
        print("账户和密码正确,请进入")
        break
    elif user == "zeng" and password == "666":
        print("账户和密码正确,请进入")
        break
    else:
        print("账户和密码错误")


# 例子二:猜数字的小游戏










