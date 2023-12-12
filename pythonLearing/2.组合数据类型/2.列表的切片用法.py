l = [1, 2, 3, 4]
print(l[0])
print(l[-1])

l[4:5] = ["x"]
print(l[:])
l[5:] = [1, 2, 3, 4, 5, 6, 7]
print(l[:])

l.append(1111)
print(l[:])

l = [1, 2, 3]
print(l + [4, 5, 6])

print(l * 3)

print(l.index(1))  # 输出第一个1的位置
print(999 in l)
print(len(l))

max(l)
min(l)
sum(l)
