def inverse_dict(my_dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    for key in inverted_dict:
        inverted_dict[key].sort()
    return inverted_dict
course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
