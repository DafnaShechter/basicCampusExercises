def last_early(my_str):
    my_str = my_str.lower() # convert all letters to lowercase
    last_char = my_str[-1] # get the last character
    if last_char in my_str[:-1]: # check if it appears before the last character
        return True
    else:
        return False


print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))