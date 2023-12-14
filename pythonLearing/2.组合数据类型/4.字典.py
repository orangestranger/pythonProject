# 字典（dict） 一种key-value映射结构，key不可重复
l = [1,]
print(type(l))
d = {1, }
print(type(d))  #set是集合
d = {"key": 1}
print(type(d))  #这才是字典
print(d['key'])  #使用
print(dict(a=1, b=2))  #第二种方法

# 判断字典是否是唯一的
d = dict(a=1, b=2, c=3, d=4)
print(d)
print(d['d'])  # 获取数据
print(d.get('a'))  # get方法
print('aa' in d)   # 判断
print(d.keys())  # 把所有的key拿出来
print('a' in d.keys())
print(d.values())  # 所有的值
print(d.items())  # 匹配好的值
print(len(d))  # 输出有几个key
print(list(d))  # 列表形式输出
print(tuple(d))

# 修改字典
print(d)
d['e']=5
print(d)
d_2 = {"x": "X", "y": "Y"}
d.update(d_2)
print(d)

d.pop('x')  # 删除需要指定key
print(d)
print(d.pop('xx', '不存在'))  #如果左边的key不在字典中，则会输出右边的值

print(d.setdefault('aa', '123'))  # setdefault设定key默认值，如果字典中没有则创建，有则输出原来key的对应值
# 清除
d.clear()
print(d)