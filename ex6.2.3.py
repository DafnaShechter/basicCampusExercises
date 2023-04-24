def format_list(my_list):
    evens = my_list[::2]
    last = " and " + my_list[-1]
    return ", ".join(evens) + last


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
formatted = format_list(my_list)
print(formatted)  # Output: hydrogen, lithium, boron, and magnesium
