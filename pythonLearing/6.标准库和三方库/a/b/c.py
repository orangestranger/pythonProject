def read_csv(file_name):
    try:
        with open(file_name, 'rt', encoding='utf-8-sig') as f:
            text = f.read()
    except Exception as e:
        print("error".format(e))

    lines = text.split("\n")

    new_lines = []

    for line in lines:
        new_line = line.split(",")
        new_lines.append(new_line)
        new_lines = [line for line in new_lines if line != ['']]  # 去除空行
    return new_lines


Title = "Hello,world"
