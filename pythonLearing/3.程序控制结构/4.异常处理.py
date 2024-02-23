#print(1)
#1/0   # 取消注释
#print(2)

# 如上代码发生异常会停止执行

#assert 1==1  # 改成1==2 生成断言
# 手动生成异常并输出自定义内容
#raise KeyError("Hello")

try:
    1/0
except Exception as e:
    print("捕捉到如下异常 {}".format(e))
