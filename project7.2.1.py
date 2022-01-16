def is_greater(my_list, n):
    big_list = []
    result = my_list
    for x in result:
        if x > n:
            big_list.append(x)
    return big_list
print(is_greater([1, 30, 25, 60, 27, 28], 28))