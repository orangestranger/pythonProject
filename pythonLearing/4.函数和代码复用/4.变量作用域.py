input = 1  # 全局作用域变量
import builtins  # 内置作用域

def f():
    input = 2  # 局部作用域变量，如果注释掉会走全局变量
    print("input in f : {}".format(input))

    print(locals()['input'])  # 直接用内置函数输出局部和全局变量
    print(globals()['input'])

    print(builtins.input)  # 内置作用域 import builtins

f()
print("a not in f : {}".format(input))
