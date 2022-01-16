def arrow(my_char, max_length1):
    max_length = int(max_length1)
    i = 0
    while max_length > i:
        i += 1
        print(my_char * i)
    while i != 0:
            i -= 1
            print(my_char * i)


charecter = input("please choos one charecter\n")
length = input("please choos length of arrow\n")
print(arrow(charecter, length))