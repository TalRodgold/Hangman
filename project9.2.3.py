def who_is_missing(file_name):
    paste = open(r"C:\Users\talro\OneDrive\Desktop\test_file1.txt", "w")
    copy = open(file_name, "r")
    num_list = copy.read()
    order = num_list.split(",")
    order.sort()
    list = []
    empty_str = 0
    for x in order:
        list.append(int(x))
    small_num = list[0]
    big_num = list[1]
    for x in list:
        if big_num - small_num == 1:
            small_num = big_num
            big_num = x + 2
        else: empty_str += (small_num - 1)
    s = str(empty_str)
    paste.write(s)




print(who_is_missing(r"C:\Users\talro\OneDrive\Desktop\test_file2.txt"))