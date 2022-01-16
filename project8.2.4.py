def sort_anagrams(list_of_strings):
    anagrams = []
    in_anagrams = []
    for x in list_of_strings:
        for y in list_of_strings:
            if sorted(x) == sorted(y):
                anagrams.append(x)
            if sorted(anagrams) == sorted(list_of_strings):
                in_anagrams.append(anagrams)
    print(in_anagrams)

לא הצלחתי!!!!!!!!!!!!!!!!!!!!!!!


list_of_words = ['deltas', 'retainers', 'desalt', 'a', 'pants', 'slated', 'generating',
'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
sort_anagrams(list_of_words)