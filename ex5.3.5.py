def distance(num1, num2, num3):
    near = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
    far = (abs(num1 - num2) >= 2 and abs(num2 - num3) >= 2) or (abs(num1 - num3) >= 2 and abs(num3 - num2) >= 2)
    return near and far


print(distance(1, 2, 10))
print(distance(4, 5, 3))