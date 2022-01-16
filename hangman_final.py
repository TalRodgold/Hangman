def main():
    print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                     6""")
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
        """Choose a word from the file.
           :param file_path: import a txt file
           :param index_str: a number given by user to choose a word from file
           :type file_path: str
           :type index_str: str
           :return: the word to guess
           :rtype: str
           """
        index = int(index_str)
        file_open = open(file_path, "r")
        file = file_open.read()
        file_list = file.split(" ")
        index_len = len(file_list)
        number_chosen = -1
        num_divide = index % index_len
        if num_divide == 0:
            number_chosen += index
        if num_divide != 0:
            resalut = num_divide
            number_chosen += resalut
        word_to_guess = file_list[number_chosen]
        return word_to_guess

    def check_valid_input(letter_guessed, old_letters_guessed):
        """ check if user input is valid.
           :param letter_guessed: input of users guess of a letter
           :param old_letters_guessed: a list of all the letters guessed
           :type letter_guessed: str
           :type old_letters_guessed: list
           :return: if the input was valid return true else return false
           :rtype: bool
           """
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
        """ print corresponding answer to user input.
            :param letter_guessed: input of users guess of a letter
            :param old_letters_guessed: a list of all the letters guessed
            :type letter_guessed: str
            :type old_letters_guessed: list
            :return: if the input was valid return true and add to list of old letters guessed else return false and print X with list of old letters guessed
            :rtype: bool
            """
        letter_guessed = letter_guessed.lower()
        old_letters_guessed.sort()
        old_letters = " -> ".join(old_letters_guessed)
        if check_valid_input(letter_guessed, old_letters_guessed) == False:
            print("X")
            print(old_letters)
            return False
        else:
            old_letters_guessed.append(letter_guessed)
            return True

    def check_win(secret_word, old_letters_guessed):
        """ check if user won the game.
            :param secret_word: the word the user is trying to guess
            :param old_letters_guessed: a list of all the letters guessed
            :type secret_word: str
            :type old_letters_guessed: list
            :return: if player won return true else return false
            :rtype: bool
            """
        for x in secret_word:
            if x in old_letters_guessed:
                continue
            if x not in old_letters_guessed:
                return False
        else:
            return True

    def show_hidden_word(secret_word, old_letters_guessed):
        """ print the word the user is trying to guess with lines.
            :param secret_word: the word the user is trying to guess
            :param old_letters_guessed: a list of all the letters guessed
            :type secret_word: str
            :type old_letters_guessed: list
            :return: replace letters with lines
            :rtype: none
            """
        new_str = ""
        space = " _ "
        for x in secret_word:
            if x in old_letters_guessed:
                new_str += " " + x
            if x not in old_letters_guessed:
                new_str += space
        print(new_str)

    file_path = input("Welcome to the Hangman game!\n\nplease enter file path here:\n")
    index = input("please choose index:\n")
    print("lets begin!\n")
    print(hangman_photos[0])
    word_to_guess = choose_word(file_path, index)
    old_letters_guessed = []
    num_of_tries = 0

    while num_of_tries <= 6:
        if check_win(word_to_guess, old_letters_guessed) == True: #check if user has won
            print(word_to_guess + "\nyou have won!")
            break
        if num_of_tries == 6: #check if user has lost
            print("LOSE")
            break
        show_hidden_word(word_to_guess, old_letters_guessed)
        current_letter_guess = input("Guess a letter:\n") #recive input from user of a letter
        current_letter_guess = current_letter_guess.lower() #make sure letter is lower case
        if try_update_letter_guessed(current_letter_guess, old_letters_guessed) == True:
            if current_letter_guess not in word_to_guess: #if the letter guessed is not in the word
                num_of_tries += 1
                print(":(")
                print(hangman_photos[num_of_tries])

if __name__ == '__main__':
    main()