def numbers_letters_count(my_str):
    result_list = [0,0]
    for x in my_str:
        if x.isdigit():
            result_list[0] += 1
        else: result_list[1] += 1
    return result_list



print(numbers_letters_count("Python 3.6.3"))