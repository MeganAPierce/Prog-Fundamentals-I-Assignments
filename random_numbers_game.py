#
# Megan Pierce                          Nov 29, 2021
# Random Number Guessing Game V2.0      Exam 3 Problem 1
#
#
#
#
import pyinputplus as pyip
import random

def play():
    
    tries = 0
    correctAnswer = int(random.triangular(1,400))
    print()

    guess = pyip.inputInt('Enter a number between 1 and 400: ',min=1,max=400)
    while guess != correctAnswer:
        if guess > correctAnswer:
            print('TOO HIGH, guess again.')
            print()
            guess = pyip.inputInt('Enter another number between 1 and 400: ',min=1,max=400)
            tries += 1
        elif guess < correctAnswer:
            print('TOO LOW, guess again.')
            print()
            guess = pyip.inputInt('Enter another number between 1 and 400: ',min=1,max=400)
            tries += 1

    print()
    print(correctAnswer,'is the right answer! Congratulations!')
    print('You made',tries,'incorrect guesses. Try to beat that!')
    print()

def main():

    player_name = intro()

    again = 'yes'
    while again == 'yes':
        play()
        again = pyip.inputYesNo('Would you like to play again? Yes or no: ')
    print('')

    print( player_name +', thank you for playing!')

def intro():
    print()
    print('{:^40}'.format('RANDOM NUMBER GUESSING GAME'))
    print('{:^40}'.format('1-400'))
    player_name = pyip.inputStr("\nEnter player name: ")
    print("\nLet's play, "+ player_name + '...\n')
    return player_name

main()
