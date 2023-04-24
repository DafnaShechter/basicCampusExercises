def squared_numbers(start, stop):
    squares = []
    num = start
    while num <= stop:
        squares.append(num ** 2)
        num += 1
    return squares


print(squared_numbers(4, 8))
print(squared_numbers(-3, 3))
