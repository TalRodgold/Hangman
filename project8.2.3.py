def mult_tuple(tuple1, tuple2):
    new_list = []
    for x in tuple1:
        for y in tuple2:
            new_list.append((x,y))
            new_list.append((y,x))
    new_list_tuple = tuple(new_list)
    return new_list_tuple

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))