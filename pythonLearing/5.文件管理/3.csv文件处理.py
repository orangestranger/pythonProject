# l_1 = [1,2,3,4,5,6,7,8,9]
# l_2 = [1,2,3,4,5,6,7,8]
# l_3 = [1,2,3,4,5,6,7]
#
# l=[l_1,l_2,l_3]
#
# print(l[-1][0])

def read_csv(file_name):
    try:
        with open(file_name, 'rt', encoding='gbk') as f:
            text = f.read()
    except Exception as e:
        print("error".format(e))

    lines = text.split("\n")
    new_lines = []

    for line in lines:
        new_line = line.split(",")
        new_lines.append(new_line)

    return new_lines

# 从csv中读取数据
# 将数据按逗号分割
data = read_csv("test.csv")
print(data)

def write_csv(file_name,lines):
    new_lines = []
    for l in lines:
        line = ".".join(l)
        new_lines.append(line)

    text = "\n".join(new_lines)
    try:
        with open(file_name, 'w', encoding='gbk') as f:
            f.write(text)
    except Exception as e:
        print("error".format(e))

data = read_csv("test.csv")
print(data)
data.append(["14","十四","forteen"])
print(data)

write_csv("test.csv", data)