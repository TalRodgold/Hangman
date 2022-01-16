temp = input("pleas enter temperature\n")
num = temp[:-1]
num_flo = float(num)
degree = temp[-1]
c = (((num_flo * 9)/5) + 32)
f = ((num_flo - 32) * 5/9)

if degree == "c" or degree == "C":
    print(c)
elif degree == "f" or degree == "F":
    print(f)
else: print ("EROR")











