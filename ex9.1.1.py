def are_files_equal(file1, file2):
    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    return content1 == content2

print(are_files_equal("c:\\animals.txt", "c:\words.txt"))