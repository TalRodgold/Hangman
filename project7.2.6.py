def get_number_from_user():
    return int(input("pleas enter a number between 1 and 9\n"))
shoping_list = input("pleas type your shoping list\n")
number = get_number_from_user()
list = shoping_list.split(",")
while number < 9:
    if number == 1:
        print(list)

    elif number == 2:
        length = len(list)
        print(length)

    elif number == 3:
        product = input("check if your product is in the list\n")
        if product in list:
            print("True")
        else: print("False")

    elif number == 4:
        product = input("check how many times your product is in the list\n")
        answer = list.count(product)
        print(answer)

    elif number == 5:
        remove1 = input("pleas choos a product you would like to remove from the list\n")
        list.remove(remove1)
        print(list)

    elif number == 6:
        add = input("pleas type a product that you would like to add to the list\n")
        list.append(add)
        print(list)

    elif number == 7:
        for x in list:
            if x.isalpha == False:
                print(x)
            elif len(x) < 3:
                print(x)

    elif number == 8:
        new_list = []
        for x in list:
            if x not in new_list:
                new_list.append(x)
        print(new_list)
    elif number == 9:
        break
    number = get_number_from_user()








