def main():
    print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                     """)
    hangman_photos = {0: " x-------x", 1: """ x-------x
 |
 |
 |
 |
 |
    """, 2: """ x-------x
 |       |
 |       0
 |
 |
 |""", 3: """ x-------x
 |       |
 |       0
 |       |
 |
 |""", 4: """ x-------x
 |       |
 |       0
 |      /|\\
 |
 |""", 5: """ x-------x
 |       |
 |       0
 |      /|\\
 |      /
 |""", 6: """ x-------x
 |       |
 |       0
 |      /|\\
 |      / \\
 |"""}

    def choose_word(file_path, index_str):
        index = int(index_str)
        file_open = open(file_path, "r")
        file = file_open.read()
        file_list = file.split(" ")
        index_len = len(file_list)
        number_chosen = -1
        if index % index_len == 0:
            number_chosen += index
        if index % index_len != 0:
            resalut = index % index_len
            number_chosen += resalut
        word_to_guess = file_list[number_chosen]
        return word_to_guess

    def check_valid_input(letter_guessed, old_letters_guessed):
        guess_len = len(letter_guessed)
        if letter_guessed in old_letters_guessed:
            return False
        elif guess_len > 1:
            return False
        elif letter_guessed.isalpha() == False:
            return False
        else:
            return True

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
            return True

    def check_win(secret_word, old_letters_guessed):
        for x in secret_word:
            if x in old_letters_guessed:
                continue
            if x not in old_letters_guessed:
                return False
        else:
            return True

    def show_hidden_word(secret_word, old_letters_guessed):
        new_str = ""
        space = " _ "
        for x in secret_word:
            if x in old_letters_guessed:
                new_str += " " + x
            if x not in old_letters_guessed:
                new_str += space
        print(new_str)

    file_path_animals = r"C:\Users\talro\OneDrive\Desktop\animals.txt"
    file_path_countries = r"C:\Users\talro\OneDrive\Desktop\countries.txt"
    file_path_food = r"C:\Users\talro\OneDrive\Desktop\food.txt"
    file_type = input("please choose a subject:\n animals    countries    food\n")
    file_path = ""
    if file_type == "animals":
        file_path = file_path_animals
    if file_type == "countries":
        file_path = file_path_countries
    if file_type == "food":
        file_path = file_path_food
    import random
    index = random.randint(1,30)
    print("lets begin!\n")
    print(hangman_photos[0])
    word_to_guess = choose_word(file_path, index)
    old_letters_guessed = []
    num_of_tries = 0

    while num_of_tries <= 6:
        if check_win(word_to_guess, old_letters_guessed) == True: #check if user has won
            print(word_to_guess + "\nWELL DONE YOU WON!")
            break
        if num_of_tries == 6: #check if user has lost
            print("the word was " + word_to_guess)
            print("YOU HAVE LOST")
            break
        show_hidden_word(word_to_guess, old_letters_guessed)
        current_letter_guess = input("Guess a letter:\n") #recive input from user of a letter
        current_letter_guess = current_letter_guess.lower() #make sure letter is lower case
        if check_valid_input(current_letter_guess, old_letters_guessed) == False: #if input is not valid
            try_update_letter_guessed(current_letter_guess, old_letters_guessed)
        if check_valid_input(current_letter_guess, old_letters_guessed) == True: #if input is valid
            try_update_letter_guessed(current_letter_guess,old_letters_guessed)
            if current_letter_guess not in word_to_guess: #if the letter guessed is not in the word
                num_of_tries += 1
                print("WRONG GUESS  :(")
                print(hangman_photos[num_of_tries])

if __name__ == '__main__':
    main()