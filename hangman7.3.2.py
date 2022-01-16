def check_win(secret_word, old_letters_guessed):
    for x in secret_word:
        if x in old_letters_guessed:
            continue
        if x not in old_letters_guessed:
            return False
    else: return True


secret_word = "eyes"
old_letters_guessed = ['e', 'y', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))
