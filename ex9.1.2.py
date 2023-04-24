def sort_words(file_path):
    with open(file_path) as f:
        words = set()
        for line in f:
            words |= set(line.strip().split())
    return sorted(words)

def reverse_lines(file_path):
    with open(file_path) as f:
        for line in f:
            print(line.strip()[::-1])

def last_n_lines(file_path, n):
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())

file_path = input("Enter a file path: ")
task = input("Enter a task: ")
if task == "sort":
    print(sort_words(file_path))
elif task == "rev":
    reverse_lines(file_path)
elif task == "last":
    n = int(input("Enter a number: "))
    last_n_lines(file_path, n)
else:
    print("Invalid task entered.")
