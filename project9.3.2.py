def my_mp4_playlist(file_path, new_song):
    file = open(file_path, "r")
    file_read = file.read()
    sorted_list = file_read.split("\n")
    replace = sorted_list[2]
    replace1 = replace.split(";")
    artist = replace1[1]
    length = replace1[2]
    empty_list = []
    empty_list.append(new_song)
    empty_list.append(artist)
    empty_list.append(length)
    fixed_list = ";".join(empty_list)
    sorted_list.pop(2)
    sorted_list.insert(2, fixed_list)
    file.close()
    paste = open(file_path, "w")
    for x in sorted_list:
        paste.write("%s\n" % x)




print(my_mp4_playlist(r"C:\Users\talro\OneDrive\Desktop\test_file1.txt", "go to hell python"))