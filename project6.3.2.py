def longest(my_list):
    new_list = sorted(my_list, key=len)
    return new_list[-1]


list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))