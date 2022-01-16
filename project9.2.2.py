def copy_file_content(source, destination):
    input = open(source, "r")
    output = open(destination, "w")
    contex = input.read()
    output.write(contex)
    output.close()

print(copy_file_content(r"C:\Users\talro\OneDrive\Desktop\test_file2.txt", r"C:\Users\talro\OneDrive\Desktop\test_file1.txt"))