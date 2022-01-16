def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    old_letters_guessed.sort()
    old_letters = " -> ".join(old_letters_guessed)
    guess_len = len(letter_guessed)
    letter_exist = letter_guessed in old_letters
    if letter_exist == True:
        print("X")
        print(old_letters)
        return False
    elif guess_len > 1:
        print("X")
        print(old_letters)
        return False
    elif letter_guessed.isalpha() == False:
        print("X")
        print(old_letters)
        return False
    elif letter_exist == False:
        old_letters_guessed.append(letter_guessed)
        print(old_letters_guessed)
        return True


letter_guessed = "a"
old_letters_guessed = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed(letter_guessed, old_letters_guessed))