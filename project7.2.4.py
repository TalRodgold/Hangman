def seven_boom(end_number):
    list = []
    last_num = end_number + 1
    for x in range(0,last_num,1):
        list.append(x)
        if "7" in str(x):
            list[x] = "BOOM"
    for num in range(0,end_number,7):
        list[num] = "BOOM"
    return list
print(seven_boom(17))