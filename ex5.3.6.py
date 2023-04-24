def filter_teens(a=13, b=13, c=13):
    def fix_age(age):
        if age >= 13 and age <= 19 and age != 15 and age != 16:
            return 0
        return age

    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c


print(filter_teens())

print(filter_teens(1, 2, 3))

print(filter_teens(2, 13, 1))

print(filter_teens(2, 1, 15))
