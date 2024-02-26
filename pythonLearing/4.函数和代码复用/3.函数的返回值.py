# def f(*v, **vvvv):
#     print(v)
#     print(vvvv)
#     print("-" * 20)
#
# a = f(1,2,3,4,5,6,7,8,9)
# print(a)

def add(a, b):
    c = a + b
    print(f"{a}+{b}=", c)
    return a, b, c  # 元组的小括号可以省略，作用是保持变量位置不变


a, b, c = add(1, 10)
res = add(c, 100)
res = add(res[2], 1000)

# python中函数一定会有一个返回值
