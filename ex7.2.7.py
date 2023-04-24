def arrow(my_char, max_length):
    arrow_list = []
    for i in range(1, max_length + 1):
        arrow_list.append(my_char * i)
        if i == max_length:
            for j in range(max_length - 1, 0, -1):
                arrow_list.append(my_char * j)
    return '\n'.join(arrow_list)


print(arrow('*', 5))