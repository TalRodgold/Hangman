def are_files_equal(file1, file2):
    txt1 = open(file1, "r")
    txt2 = open(file2, "r")
    txt11 = txt1.read()
    txt22 = txt2.read()
    if txt11 == txt22:
        return True
    else: return False





print(are_files_equal(r"C:\Users\talro\OneDrive\Desktop\test_file1.txt", r"C:\Users\talro\OneDrive\Desktop\test_file2.txt"))