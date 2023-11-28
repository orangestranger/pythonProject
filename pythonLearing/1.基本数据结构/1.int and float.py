# type可以输出类型 int为整型 float是浮点型
print(type(1))  # 会输出int
print(type(1.1))  # 会输出float
print(type(1+1))  # 会输出int
print(type(1+1.1))  # 会输出float
print(type(1+1.0))  # 会输出float

print(type(1*1.0))  # 乘法会输出浮点型
print(type(1**1.0))  # 还是会输出浮点型

print(type(2/2))  # 除法会输出浮点型

print(type(3//2))  # 两个//符号：整除，可以使除出来的类型变为整型
print(type(4%2))

print(abs(1))  # abs函数
print(abs(-1))  # 输出绝对值

print(pow(3, 3))  # 求幂
print((3**3))  # 表达式

print(divmod(10,3))  # 求商和余数
print(max(1, 2, 3, 4, 5, 6))  # 求最大值
print(min(1, 2, 3, 4, 5, 6))  # 求最小值

print(10/2.0)  # float
print(10*20.0)  # float
