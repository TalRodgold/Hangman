def is_valid_input(letter_guessed):

    guess_len = len(letter_guessed)
    letter = letter_guessed.isalpha()
    if guess_len > 1 and letter == False:
        return False
    elif guess_len > 1:
        return False
    elif letter == True:
        return letter_guessed.lower()
    elif letter == False:
        return False
print(is_valid_input(#guess letter here))
