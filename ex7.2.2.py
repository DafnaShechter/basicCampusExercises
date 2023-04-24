import string


def numbers_letters_count(my_str):
    digits = 0
    letters = 0

    for char in my_str:
        if char.isdigit():
            digits += 1
        elif char.isalpha() or char.isspace() or char in string.punctuation:
            letters += 1

    return [digits, letters]

print(numbers_letters_count("Python 3.6.3"))