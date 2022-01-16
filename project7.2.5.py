def sequence_del(my_str):
    new_str = ""
    current_letter = ""
    for x in my_str:
        if x != current_letter:
            new_str += x
            current_letter = x
    print(new_str)

sequence_del("Heeyyy   yyouuuu!!!")
