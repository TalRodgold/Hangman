guess = input("GUESS A LETTER:\n")
guess_len = len(guess)
letter = guess.isalpha()
if guess_len > 1 and letter == False:
    print("E3")
elif guess_len > 1:
    print("E1")
elif letter == True:
    print(guess.lower())
elif letter == False:
    print("E2")
