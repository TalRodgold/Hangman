def chocolate_maker(small, big, x):
    b = big * 5
    if (small + b) >= x:
        return True
    else: return False
print(chocolate_maker(3, 1, 9))