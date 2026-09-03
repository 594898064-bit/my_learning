

# | 方法       | 作用               | 样例           |
# | append() | 在列表的尾部追加元素 | s.append(10086) |
# | insert() | 在指定索引之前，插入该元素 | s.insert(0, 92) |
# | remove() | 移除列表中第一个匹配到的值 | s.remove(75) |
# | pop() | 删除列表中指定索引位置的元素（如果未指定索引，默认删最后一个） | s.pop(2) / s.pop() |
# | sort() | 对列表进行排序（列表元素的数据类型一致，才可以进行排序） | s.sort() |
# | reverse() | 反转列表元素 | s.reverse() |
s = [203,908,798,908,543]
# 尾部追加元素
s.append(10086)
print(s)
# 插入元素
s.insert(2,100)
print(s)
# 移除元素
s.pop(-3)
print(s)
# 列表排序
s.sort()
print(s)
# 反转元素
s.reverse()
print(s)