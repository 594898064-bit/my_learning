# 列表
# 定义列表 - list
s = [56,90,88,65,90,"A","Hello",True]

print(type(s))


# 访问列表
# 获取
print()
# 正向索引  从0开始
print(s[0])
#反向索引  从-1开始
print(s[-8])
# 修改
s[5] = "abc"
print(s)


# 删除
del s[5]
print(s)



# 遍历
for item in s:
    print(item)



# 总结:
#  查看:list[0]
#  修改:list[0] = "A"
#  删除:del list[3]



