def format_list(my_list):
    zugi = my_list[0:-1:2]
    last = my_list[-1:]
    final = [" ,".join(zugi)]
    new_list = final + last
    final_list = " and ".join(new_list)

    return final_list

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))