data = ("self", "py", 1.543)
format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
print(format_string.format(data[0], data[1], data[2]))
