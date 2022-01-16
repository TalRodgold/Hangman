question = input("enter a word\n")
r_to_l = question[::1]
l_to_r = question[-1::-1]
if r_to_l == l_to_r:
    print("ok")
else: print("not")


