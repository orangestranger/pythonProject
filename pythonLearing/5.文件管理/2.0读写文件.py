def main():
    try:
        filename = "text.txt"
        with open(filename, "tr+", encoding="utf8") as f:
            f.write(input(""))
    except Exception as e:
        print("baocuo： {}".format(e))

main()



