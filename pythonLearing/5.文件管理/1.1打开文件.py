def main():
    filename = input("input:")
    try:
        with open(filename, "x") as f:
            print("创建成功")
            pass
    except Exception as e:
        print("创建失败，文件已经存在： {}".format(e))


# main()


def openfile():
    filename = "text.txt"
    with open(filename, "tr", encoding='utf8') as t:
        print(t.read())
    with open(filename, "rb",) as b:
        print(b.read())

openfile()
