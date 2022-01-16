def distance(num1, num2, num3):
    num2p1 = abs(num2) - 1
    num3p1 = abs(num3) - 1
    num2p2 = abs(num2) - 2
    num3p2 = abs(num3) - 2
    if (num2p1 == num1 or num3p1 == num1) and  (num2p2 > num1 or num3p2 > num1):
        print("true")
    else: print("false")

num1, num2, num3 = #enter numbers here
print(distance(num1, num2, num3))


