def choose_word(file_path, index):
    f = open(file_path, "r")
    file = f.read()
    file_list = file.split(" ")
    counting_list = []
    resault_tuple = []
    for x in file_list:
        if x not in counting_list:
            counting_list.append(x)
    first_answer = len(counting_list)
    resault_tuple.append(first_answer)

    index_len = len(file_list)
    number_chosen = -1
    if index % index_len == 0:
        number_chosen += index
    if index % index_len != 0:
        resalut = index % index_len
        number_chosen += resalut
    secend_answer = file_list[number_chosen]
    resault_tuple.append(secend_answer)
    final = tuple(resault_tuple)
    return final



print(choose_word(r"C:\Users\talro\OneDrive\Desktop\hangman_word_list.txt",15))