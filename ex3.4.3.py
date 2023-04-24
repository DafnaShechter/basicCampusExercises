user_input = input("Please enter a string: ")
half_length = len(user_input) // 2
new_string = user_input[:half_length].lower() + user_input[half_length:].upper()
print(new_string)
