if True:
    print('true')
else:
    print('false')

if False:
    print('true')
else:
    print('false')

if 1:  # 隐式转换成布尔值
    print('true')
else:
    print('false')

if 0:  # 隐式转换成布尔值
    print('true')
else:
    print('false')

# 关系运算符号的优先级高于逻辑运算符
# 关系运算符：!=, ==, is, is not, in, not in, >, >=, ==, <, <=
# 逻辑运算符：and, or, not

print(True and False)
print(True and True)  # 左右都为真才会输出真
print(False and True)

print(True or False)
print(False or True)  # 有一边为真则为真
