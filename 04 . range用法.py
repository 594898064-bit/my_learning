# 用法一:
# range (end)--> 获取一个从0开始 到end结束的数字系列(不含end本身)
# range (5)获取的数据就是0 1 2 3 4
# 用法二:
# range(start ,end) ->获取一个从而start开始到end结束的数字系列(不含end本身)
# range(2,8)获取的数据据就是2,3,4,,5,6,
# 用法三:range(start,end,step) ->获取一个从sstart开始,到end结束的数字序列,step步长(不含end本身)
# range(start,end,step) _>获取一个从start开始,到end结束的数字序列,step步长(不含end本身)
# range(0,10,2)获取的数据就是0,,2,4,6,8


# 作业:基于for循环完成如下需求:
# 1 . 计算1-100之间的所有奇数的和
# 2 . 计算100-500之间的所有3的倍数的数字之和
total=0
for i in range(1,101):
    if i%2!=0:
        total = total + i
    i=i+1
else:
    print(f"1-100之间的所有奇数的和:{total}")


total=0
for i in range(100, 501):
    if i % 3==0:
        total = total + i
    i=i+1
else:
    print(f"1-100之间的所有奇数的和:{total}")