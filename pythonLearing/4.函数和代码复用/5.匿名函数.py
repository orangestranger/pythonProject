# 没有名字的函数，由lambda表达式创建
# 1.只有参数和函数体，没有函数名
# 2.函数体内只有表达式，没有注释和复合语句

def f(add):
    print("收到函数{}".format(add))
    print("调用函数{}".format(add(1,2)))


f(lambda a, b: a + b)  # 创建匿名函数
