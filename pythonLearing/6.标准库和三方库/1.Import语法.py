# 模块（modules)
# 是包含函数、类、常量、变量等，名称符合Python标识符要求的代码文件，使用.py结尾

# 包（package)
# 名称符合Python标识符,是一个目录，目录下包含__init__.py和其他模块、包文件，__init__.py文件是包初始化文件，__init__.py文件可以不写，但是目录下必须有__init__.py文件

# 库（library)
# 是一个包含模块的包，使用.pyd结尾

# 第一种引用
# import a.b.c
# print(a.b.c.Title)
# data = a.b.c.read_csv('test.csv')
# print(data)

# 第二种引用
# from a.b import c
# print(c.Title)
# data = c.read_csv('test.csv')
# print(data)

# 第三种引用
# from a.b.c import *
# print(Title)
# data = read_csv('test.csv')
# print(data)