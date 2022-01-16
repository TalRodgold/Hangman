def count_chars(my_str):
    dict = {}
    for x in my_str:
        dict[x] = my_str.count(x)
    del dict[" "]
    print(dict)



magic_str = "abra cadabra"
count_chars(magic_str)