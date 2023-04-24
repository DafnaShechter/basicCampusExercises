def count_chars(my_str):
    char_dict = {}
    for char in my_str:
        if char != ' ':
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict
magic_str = "abra cadabra"
char_counts = count_chars(magic_str)
print(char_counts)
