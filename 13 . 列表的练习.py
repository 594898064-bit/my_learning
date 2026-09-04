# 1. 生成一个1-20的平方列表
# 2 . 从如下的数字列表中提取所有的偶数,并计算其平方,组成一个新的列表.
# 方法一:
from operator import ifloordiv

num_list =[]

for i in range(1,21):
    num_list.append(i**2)

print(num_list)

# 方式二:列表推导式  --->就是按照一定的规则生成一个列表的方法-->语法的格式:[要插入的值 for i in 序列/列表]
num_list2 = [i**2 for i in range(1,21) ]
print(num_list2)

# 案例3:从一个数字列表中提取所有的偶数,并计算其平方,组成一个新的列表

num_list1 = [12,14,15,27,78]
num_list2 = []
for num in num_list1:
    if num % 2 == 0:
        num_list2.append(num**2)
        print(num_list2)



# 列表推导式-->就算是按照一定的规则快速生成一个列表的方法-->语法格式2:[要插入的值for i in 序列/列表 if 条件]
num_list = [12,14,15,27,78]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)





# ----------重要,very improtant
# 1. 将如下多个列表合并为一个列表，并去重复元素，排序（升序）后输出到控制台。

# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排序后输出到控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'Q']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
#
#
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'Q']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
new_list = []
num_list = [*list1, *list2, *list3]
print(num_list)
for num in num_list:
    if num not in new_list:
        new_list.append(num)
