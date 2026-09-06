# 1 . 输入一个字符串,判断该字符串上是否为回文(两边对称)
# 黄山落叶松叶落日黄
# 上海自来水来自海上
# 2 . 将用户输入的10个字符串,反转后全部转换为大写,然后记录在列表中,最后将列表内容遍历输出出来
str = input("请输入一串文字:")
if str[::-1]==str:
    print("该段文字是回文字符串")
else:
    print("该段文字不是回文字符串")



new_list = [ ]
for i in range(10):
    chat = input(f"请输入第{i+1}个字符：")
    if chat not in new_list:
        new_list.append(chat)
new_list.reverse()
su = new_list.upper()
print(f"{su}")

    # for i in range(10):
    #     char = input("请输入第" + str(i + 1) + "个字符：")
    #     char_list.append(char)
    #
    # char_list.reverse()
    #
    # for char in char_list:
    #     print(char.upper())