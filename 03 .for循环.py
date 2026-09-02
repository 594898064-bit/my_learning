# for循环 循环遍历机制
from functools import partial
from traceback import print_tb

msg = input("请输入你需要遍历的文本")
for s in msg:
    print(f"元素:{s}")
else:
    print("已完成遍历")
# 总结:while:用于在某个条件满足时一直循环,,循环的次数通常是未知的,只知道循环的开始/结束的条件
# for:用于对一个一致的数据进行遍历或已知次数的循环



# 作业:基于for循环完成如下需求:
# 1 . 计算1-100之间的所有奇数的和
# 2 . 计算100-500之间的所有3的倍数的数字之和
# part 1.
total = 0
i = 0
while i <=100:
    if i%2 !=0:
        total = total + i
    i = i + 1
else :
    print(f"1-100奇数之和是:{total}")
# part 2.
#要使用一个range函数用来列举出那些数字