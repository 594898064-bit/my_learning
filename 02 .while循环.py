# 循环 通过条件表达式 控制下一次的循环
i = 0
while i<10:
    print("人生苦短我用python")
    i += 1
else :
    print("语法错误")
    # 例子
# 计算1_100之间的所有偶数之和
total = 0
i = 1
while i <=100:
    if i %2==0:
         total = total + i
    i+=1

print(f"1_100之间的所有偶数之和:{total}")