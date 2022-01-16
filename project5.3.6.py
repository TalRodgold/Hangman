def fix_age(a):
    if (13 <= a <= 19) and a != 15 and a != 16:
        a = 0
    return a


def filter_teens(num1=13, num2=13, num3=13):
    age1 = fix_age(num1)
    age2 = fix_age(num2)
    age3 = fix_age(num3)
    sum = age1 + age2 + age3
    return sum


print(filter_teens(1, 14, 15))
