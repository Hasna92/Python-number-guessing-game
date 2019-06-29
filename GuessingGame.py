play = 'yes'
while play == 'yes':
    
    import random
    numtoguess = random.randint(0,100)
    print(' Welcome to the Python powered guessing game!\n You will have to guess an integer between 1 to 100.\n If your guess is within 10 of the number, you will get a warm signal!\n If not you get a cold warning! All subsequent warnings will tell you if you are getting warmer or colder!\n Good luck!')

    guesses = []
    while True:
        guess = int(input('Whats your guess? '))
        if guess == numtoguess:
            guesses.append(guess)
            print('You win! It only took you {} guess!'.format(len(guesses)))
            break
        if guess<1 or guess >100:
            print('That guess is OUT OF BOUNDS! Try again!')
            continue
        if  -10 <= guess-numtoguess <= 10:
            print('You are warm!')
            guesses.append(guess)
            break
        else:
            print('You are cold :(')
            guesses.append(guess)
            break
    
    while True:
        guess = int(input('Whats your guess? '))
        if guess<1 or guess >100:
            print('That guess is OUT OF BOUNDS! Try again!')
            continue
        guesses.append(guess)
        if  abs(guesses[-2]-numtoguess) >= abs(guess-numtoguess)  :
            if guess == numtoguess:
                print('You win! It only took you {} guesses!'.format(len(guesses)))
                break
            else:
                print('you are warmer!')
                continue
        else:
            print('You are colder! :(')
            continue
    
    play = str(input('Want to play again? Anwer yes or no      '))
