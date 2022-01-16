def show_hidden_word(secret_word, old_letters_guessed):
    new_str = ""
    space = " _ "
    for x in secret_word:
        if x in old_letters_guessed:
            new_str += " " + x
        if x not in old_letters_guessed:
            new_str += space
    return new_str



secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))