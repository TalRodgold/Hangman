sen = input("pleas enter any scentence\n")
b = len(sen)
if b == 0 or b > 20:
    print("rong input")

else:
    a = sen[1:].replace(sen[0], "e")
    print(sen[0] + a)









