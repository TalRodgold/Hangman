def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x
list_x = [4, 5, 6]
list_y = [1, 2, 3]
print(extend_list_x(list_x, list_y))