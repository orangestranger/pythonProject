# def hello(hi, name="world", hihi="123"):
#     print(hi, name, hihi)
#
#
# hello(hi="hello")

# def f(l={}):
#     l.append(1)
#     print(l)
#
#
# f()
# f()
# f()

def f(*args, **kwargs):
     print(args, kwargs)  # 元组，字典


f(1,2,3)
f(key="key")
f()