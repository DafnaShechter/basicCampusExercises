def copy_file_content(source, destination):
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        content = f1.read()
        f2.write(content)


copy_file_content("c:\\animals.txt", "c:\words.txt")