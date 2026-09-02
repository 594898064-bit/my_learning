# print自带换行效果
# 不换行的做法print("*",end=" ")
# 写出一个长度为10,,宽度为5 的长方形
m = int(input("写输入长方形的长度:"))
n = int(input("写输入长方形的宽度:"))
for s in range(n):
    for i in range(m):
        print("*",end=" ")
    print()


# 作业   打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}x{j}={i*j}",end="\t")
    print()



for i in range(6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")


for i in range(1,7):
    for j in range(1,i):
        print(f"{j}",end=" ")
    print()





