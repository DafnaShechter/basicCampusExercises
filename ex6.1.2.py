def shift_left(my_list):
    """
    Shifts a list one step to the left and returns the new list.

    Parameters:
    my_list (list): A list of length 3.

    Returns:
    list: A new list with the elements shifted one step to the left.
    """
    return my_list[1:] + [my_list[0]]


def main():
    print(shift_left([0, 1, 2]))
    print(shift_left(['monkey', 2.0, 1]))


if __name__ == "__main__":
    main()
