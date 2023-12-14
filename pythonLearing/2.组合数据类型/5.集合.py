# 集合(set) key是value的字典
s = {1, 1, 1, 2, 3, 4, 5, 6}
print(s)  # 重复的值会覆盖 去重

l = [1,2,3,1,2,3]
print(set(l))

s.add(7)
print(s)

s.remove(1)
print(s)

