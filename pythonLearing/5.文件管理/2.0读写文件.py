def main():
    # try:
    #     filename = "text.txt"
    #     with open(filename, "x") as f:
    #         print("{}".format(filename))
    # except Exception as e:
    #     print("文件已经存在{}".format(e))
    #     pass
    try:
        filename = "text.txt"
        with open(filename, "tr+", encoding="utf8") as f:
            # f.write(input("请直接输入:"))
            text = f.readlines()
            l = list(text)
            print(l)

    except Exception as e:
        print("baocuo： {}".format(e))

main()



# read([n])      按长度读取内容
# readline()     按行数读取内容
# readlines()    按行遍历内容
# write(s)      写入指定内容
# writeslines()  按行写入内容
