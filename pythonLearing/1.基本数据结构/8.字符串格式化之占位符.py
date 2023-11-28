a = 2
b = 3
print(a)
print("1 %s 3" % a)
print("1 {}  3".format(a))  # {}占位符 ,冒号内的字符串为模板字符串，将来的变量会在占位符中出现

from string import Template
print(Template("1 $a 3").substitute(a=2))


s = " {}  cyz"
print(s.format("fyy"))

c = "{} {}"
print(c.format("fyy", "cyz"))  # 有几个占位符就必须要对应几个值

d = "{0} {2}"  # 可以通过数字来选择值
print(d.format("fyy", "cyz", "sb"))

print("我{fuck}你{mom}，有本事来揍你{grandpa}我，我直接{kick}送你上西天".format(fuck="操", mom="妈", grandpa="爷爷", kick="一库"))
