def mult_tuple(tuple1, tuple2):
    return tuple((a, b) for a in tuple1 for b in tuple2) + tuple((b, a) for a in tuple1 for b in tuple2)
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
result_tuple = mult_tuple(first_tuple, second_tuple)
print(result_tuple)
