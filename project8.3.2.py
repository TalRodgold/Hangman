number = int(input("pleas choos a number\n"))
dic = {"first_name": "mariah", "last name": "carey", "birth_date": "23.03.1970", "hobbies": ["sing", "compose", "act"]}
hobbies_list = dic["hobbies"]
if number == 1:
    print(dic["last name"])
if number == 2:
    print(dic["birth_date"])
if number == 3:
    print(len(dic["hobbies"]))
if number == 4:
    print(hobbies_list[-1])
if number == 5:
    hobbies_list.append("coocking")
    print(hobbies_list)
if number == 6:
    split = dic["birth_date"].split('.')
    birth_date_tuple = tuple(split)
    print(birth_date_tuple)
if number == 7:
    dic["age"] = "50"
    print(dic)
