a = 0


while a < 2:
    content = input("请输入内容：")
    print(content)
    a = a + 1

print("end")  # 跳出循环，缩进到底，上面循环体是四个空格


l = [1,2,3,4,5,6]
r = range(1,100)
for i in r:  # i这个值可以用在列表、元组、字符串、字典
    print(i)

