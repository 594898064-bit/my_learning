# 例子二:猜数字的小游戏
# 系统随机生成一个随机数
# 用户根据提示猜数字，并将所猜的数字输入系统
# 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 如果猜对，系统自动退出，游戏结束

import random
random_num = random.randint(1,100)


while True:
    num = int(input("请输入一个数字:"))
    if num > random_num:
        print("你输入的数字太大了")
        continue
    if num < random_num:
        print("你输入的数字太小了")
        continue
    else:
        print("输入正确")
        break
print("正确答案是:", random_num)

