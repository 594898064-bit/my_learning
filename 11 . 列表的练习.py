# ----------------------------列表的案例---------------------------
# 案例一:将用户的输入的10个数字,存储到一个列表里面进行排序,输入其中的最小值,最大值和平均值
# 定义一个空列表
num_list = [ ]

# 将用户的输入的10个数字存入列表
for _ in range(10):
    num = int(input("请输入一个有效的数字:"))
    num_list.append(num)
# 虽然有 i，但是下面没有写 i，所以它只是负责接收 range(10) 每次产生的数字，本身没有参与后面的操作。
#
# 实际上可以写成：
# for _ in range(10):
#     num = int(input("请输入一个有效的数字:"))
#     num_list.append(num)
# i 是循环计数器，可以用来知道“现在是第几次循环”；如果不需要知道，就可以用 _ 代替。
print("这是个数字是:",num_list)
num_list.sort()
print("这几个数里面的最小值",num_list[0])
print("这几个数里面的最大值",num_list[-1])
print("这几个数字的平均值",sum(num_list)/len(num_list))
# len是length的简称所以表示的意思是长度


# min()获取最小值
# max():获取最大值
# sum:求和
# len:计算长度