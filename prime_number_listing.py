# Megan Pierce                      Oct 13, 2021
# Prime Numbers V1                  Ch 7, Problem 12
#
#
# A positive integer greater than 1 is said to be PRIME if it has no divisors other than
# 1 and itself. Write a program that asks the user to enter an integer greater than 1, then displays
# all of the prime numbers that are LESS THAN or EQUAL TO the number entered.

import pyinputplus as pyip
import math

def introduction():
    print()
    print('{:^99}'.format('PRIME NUMBER LIST'))
    print()
    print("This program will give you all prime numbers that exist up to your given number, between 2 and 500.")
    print('{:^99}'.format("If the number you provide is not in the list, it is not prime."))
    print()

#function to get number from user and validate their input
def user_input():
    userNumber = pyip.inputInt('Give me a number greater than 1 and less than 500: ',min=2,max=500)
    if userNumber < 1:
        userNumber = pyip.inputInt('Need a number GREATER than 1. Please provide another number: ')
    else:
        return userNumber

def determine_prime(userNumber):
    primeList = []
    number = 0 #list integer
    for number in range(2,userNumber+1):
        if all(number % i !=0 for i in range(2,int(math.sqrt(number))+1)):
            primeList.append(number)
            number +=1
    return primeList

def print_statement_ii(userNumber, primeList):
    print('Prime numbers before and up to ',userNumber,':',sep='')
    for i, item in enumerate(primeList):
        if (i+1)%10 == 0:
            print(item)
        else:
            print(item, end=' ')

def main():
    introduction()
    runAgain = 'yes'
    while runAgain == 'yes':
        userNumber = user_input()
        primeList = determine_prime(userNumber)
        print_statement_ii(userNumber, primeList)
        print()
        runAgain = pyip.inputYesNo('Do you want to run this again with a new number? YES or NO: ')
        print()
    print('Thank you for using PRIME NUMBER LIST.')


main()