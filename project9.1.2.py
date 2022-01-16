task_chosen = input("pleas choos one option: sort, rev, last\n")
file = open(r"C:\Users\talro\OneDrive\Desktop\test_file1.txt", "r")
txt1 = file.read()
list = txt1.split()
empty_list = []
if task_chosen == "sort":
    for x in list:
        if x not in empty_list:
            empty_list.append(x)
    empty_list.sort()
    print(empty_list)
if task_chosen == "rev":
    print(txt1[::-1])
if task_chosen == "last":
    num = input("pleas choos number of lines\n")

    print(file.readlines(2))

