# 条件循环 while
# a = 0
#
# while a < 3:
#     content = input("请输入内容：")
#     print(content)
#     a = a + 1
#     print(f"已经超时{a}次")

# 遍历循环 for
# l = [1, 1, "x", .1]
# r = range(1, 100)
# for i in l:  # l这里可以遍历值并且赋值给i l的类型可以是列表，元组，字符串，字典
#     print(i)

# 循环控制 （break中止, continue快进)
while True:
    content = input("请输入内容：")
    if content == "continue":
        continue  # 直接进行下一次循环，不走下面的代码
    elif content == "exit":
        break
        print(content)
