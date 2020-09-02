def guessLoopAnimal():
    print("This Animal is becoming the king of the land")

    secret_word = "LION"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you lose!")
    else:
        print("you win!")

def guessLoopJob():
    print("Eat Donuts and Coffee and also catching the robbery")
    secret_word = "POLICE"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you lose!")
    else:
        print("you win!")

def guessLoopStudy():
    print("The worst subject but truly important for our life")
    secret_word = "MATH"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you lose!")
    else:
        print("you win!")

def guessLoopFood():
    print("Minang traditional food")
    secret_word = "RENDANG"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you lose!")
    else:
        print("you win!")

def guessStart():
    print("1. Animal\n2. Study\n3. Profecy\n4. Food")
    choiceTheme = input("choose your theme and go ahead: ")
    print("=====================================")
    if choiceTheme == "1" :
        guessLoopAnimal()
    elif choiceTheme == "2":
        guessLoopStudy()
    elif choiceTheme == "3":
        guessLoopJob()
    elif choiceTheme == "4":
        guessLoopFood()


print("\nWELCOME TO THE MYSTERY GUESS!\n\nPLEASE CHOOSE THE THEME\n=====================================\nANSWER THE QUIZ USING UPPERCASE\n=====================================")
guessStart()