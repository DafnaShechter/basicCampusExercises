string = input("Please enter a string: ")

if len(string) > 0:
    first_char = string[0]
    new_string = first_char + string[1:].replace(first_char, 'e')
    print(new_string)
else:
    print("The string is empty.")
