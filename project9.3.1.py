def my_mp3_playlist(file_path):
    file = open(file_path, "r")
    file_read = file.read()
    sorted = file_read.split("\n")
    empty_tuple = []
    list = []
    for x in sorted:
        list.append(x.split(";"))
    dict_items = {"songs": [], "name": [], "length": []}
    for item in list:
        if len(item) >= 3:
            dict_items["songs"].append(item[0])
        if len(item) >= 2:
            dict_items["name"].append(item[1])
        if len(item) >= 1:
            dict_items["length"].append(item[2])
    longest = dict_items["songs"][dict_items["length"].index(max(dict_items["length"]))]
    empty_tuple.append(longest)
    num_of_songs = len(dict_items["songs"])
    empty_tuple.append(num_of_songs)
    singer = []
    for x in dict_items["name"]:
        singer.append(dict_items["name"].count(x))
    location_singer = singer.index(max(singer))
    empty_tuple.append(dict_items["name"][location_singer])
    final = tuple(empty_tuple)
    return final


print(my_mp3_playlist(r"C:\Users\talro\OneDrive\Desktop\test_file1.txt"))