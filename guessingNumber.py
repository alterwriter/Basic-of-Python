import random

play_game = 'y'

while (play_game=='y'):
    answer = random.randint(1, 100)
    try_number = input('Guess a number between 1 and 100 : ')
    try_number = int(try_number)
    counter = 1

    while try_number != answer:
        if try_number > answer:
            print('your number is too large')
        if try_number < answer:
            print('Your number is too small')
        try_number = int(input('Guess again : '))
        counter += 1
    
    print('You got it! you tried ' + str(counter)+ ' times')
    play_game = input('continue? ')