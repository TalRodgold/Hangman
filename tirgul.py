num1 = input("enter number\n")
num2 = input("enter number\n")
num3 = input("enter number\n")
biggest = 0
smallest = 0
middle = 0
if num1 > num2:
    if num1 > num3:
        if num3 > num2:
            biggest = num1, middle = num3, smallest = num2
        else:
            biggest = num1, middle = num2, smallest = num3
    else:
        biggest = num3, middle = num1, smallest = num2
else:
    if num2 > num3:
        if num3 > num1:
            biggest = num2, middle = num3, smallest = num1
        else:
            biggest = num2, middle = num1, smallest = num3
    else:
        biggest = num3, middle = num2, smallest = num1
print("biggest is ",biggest)
print("middle is ",middle)
print("smallest is ",smallest)

