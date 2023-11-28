s = "abcdef"
print(s)

print(s[0])
print(s[1])
print(s[0], s[1], s[2])
print(s[0:2])
print(s[0:3])
print(s[1:3])  # 包左不包右

print(s[0:])  #结尾和开头可以用空
print(s[:])

print(s[0:6:1])   # 第三个数字是用来表示从a到b的跨度，如果是2，则为a，c，e
print(s[0:6:2])
