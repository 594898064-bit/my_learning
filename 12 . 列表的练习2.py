# # 合并两个列表的元素,并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [1,2,3,4,5,6,7,8,9,10]
# num_list2 = [1,4,5,6,7,8,9,10,11,12]
#
# # 1 . 合并列表
# for num in num_list2:
#         num_list1.append(num)
# print("列表的原始元素是:",num_list1)
#
# # 2. 去除重复元素
# new_list = []
#
#
# for num in num_list1:
#     if num  not in new_list :
#         new_list.append(num)
# print("除重之后的列表为:",new_list)





# 案例2 . 简单版
# 合并两个列表的元素,并对合并的结果进行去重处理(去除列表中的重复元素)
num_list1 = [1,2,3,4,5,6,7,8,9,10]
num_list2 = [1,4,5,6,7,8,9,10,11,12]

# 1 . 合并列表
# 解包:将列表这一类容器解开为一个一个的独立的元素   或者是中间加一个加号
# 组包:将多个值合并到一个容器

num_list = [*num_list1,*num_list2]
# 把 A 和 B 拆开，然后装进同一个新列表。
print("列表的原始元素是:",num_list1)

# 2. 去除重复元素
new_list = []


for num in num_list1:
    if num  not in new_list :
        new_list.append(num)
print("除重之后的列表为:",new_list)

