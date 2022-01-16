def are_lists_equal(list1, list2):
    check_list1 = sum(list1)
    check_list2 = sum(list2)
    if check_list1 == check_list2:
        return True
    else: return False

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list3))