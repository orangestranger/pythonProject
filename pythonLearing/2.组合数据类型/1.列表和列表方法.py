a = "ppp-lll-qqq".split("-")  # 分割字符串，结果称之为列表
print(a)
print(type([a]))

b = [1, 0.1, 4567+123j, "cyz"]  # 中括号中是列表
print(type(b))

# 增删列表元素的方法
o = [1, 2, 3]
print(o)
o.append(4)  # 在末尾添加
print(o)
o.insert(0, "x")  # 添加第一位
print(o)
o.pop()  # 删除最后一位
print(o)
o.pop(0)  # 删除指定地方的值
print(o)
o.remove(2)  # remove方法需要写实际的值，找不到则报错，且只会删除第一个值，后续不会删除
print(o)

l = [1, 1, 2, 2, 3]
print(l.index(1))  # 匹配到第一位的值，输出位置

print(l.count(1))  # 计数1出现了几次

l = [1, 4, 7, 1, 34, 6, 89, 22]
l.sort()  # 排序
print(l)
l.reverse()  # 从大到小排序
print(l)