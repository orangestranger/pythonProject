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

