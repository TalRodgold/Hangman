def check_valid_input(letter_guessed, old_letters_guessed):
    guess_len = len(letter_guessed)
    if letter_guessed in old_letters_guessed:
        return False
    elif guess_len > 1:
        return False
    elif letter_guessed.isalpha() == False:
        return False
    else: return True


old_letters_guessed =["a", "b", "c"]
letter_guessed = "t"
print(check_valid_input(letter_guessed, old_letters_guessed))