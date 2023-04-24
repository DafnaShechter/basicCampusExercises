def chocolate_maker(small, big, x):
    if x > (small + big * 5):
        return False
    elif x % 5 > small:
        return False
    else:
        return True


print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))