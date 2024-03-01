# f = open(r'C:\Users\o3846\Desktop\123.txt')
# print(f.read())
# f.close()
# 打开文件
with open(r'C:\Users\o3846\Desktop\123.txt', mode="r+") as f:  #函数结束后会认为方法已经结束，不用写close
    print(f.read())

# 文件打开模式的例子
# 'r'    read       读取(默认）
# ‘w’    write      写入
# 'a'    append     追加内容
# ‘x'    exclusive  独占写入，如果文件存在则报错
# ’b‘    binary     二进制模式
# ’t‘    text       文本模式（默认值）
# ’+‘    扩展        扩展为读写模式

# 1.文本内容
# 读取内容 tr
# 追加内容 ta
# 覆盖内容 tw
# 创建新文件 tx

# 2.二进制内容
# 读取内容 br
# 覆盖内容 bw
# 创建新内容 bx

# 3.读写模式
# 读取内容 br+  不能写bw+,不然文件会清空打开

open(mode=r+"w", encoding="")