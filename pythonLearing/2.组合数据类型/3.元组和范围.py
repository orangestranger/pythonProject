# 元组（tuple）= 不可变的列表
t = (1, 2)
print(type(t))

print(t.index(2))
print(t.count(1))
print(t[0])
print(t[:])

# t[0:] = "x"  # 会报错

# 范围(range) 只包含整数的元组
range(9)
print(type(range(9)))
print(range(9))
range(1, 9)
print(range(1, 9))
print(list(range(1, 9)))

r = range(1, 10, 2)
print(r)
print(list(range(1, 10, 2)))  # 这里的2代表间隔

t = [1,2,3,4,5,6,7,8,9]
import sys
print(sys.getsizeof(t))
t = [1,2]
print(sys.getsizeof(t))
t = range(9)
print(sys.getsizeof(t))
t = range(999)  # range占内存是一样的
print(sys.getsizeof(t))