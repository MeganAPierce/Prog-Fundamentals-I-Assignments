# Suppose you have money in a savings account that earns
# compound month interest
# F=Px(1+i)^t

# F = the future value of the account after specified time period
# P = the present value of the account
# i = the monthly interest rate
# t = the number of months

# Write a program that will provide the value of the account after
# user inputs starting value and months..

import pyinputplus as pyip

def program_header():
    print()
    print('{:^91}'.format('ACCOUNT FUTURE VALUE CALCULATOR'))
    print('This program will tell you how much your account will be worth '
          'in a given number of months.')
    print()

def userInput():
    presentVal = pyip.inputFloat('What is the current value of your account? ')
    interest_rate = pyip.inputFloat('What is your interest rate? Input as a decimal number: ')
    moInterest = (interest_rate/12)    #interest is accrued monthly, must divide by 12
    numOfMonths = pyip.inputFloat('How many months do you wish to accrue interest? ')
    print()
    print()
    return presentVal, moInterest, numOfMonths

def calculate_futureValue(presentVal, moInterest, numOfMonths):
    futureValue = presentVal*((1+moInterest)**numOfMonths)
    return futureValue

def output(futureValue):
    print('The FUTURE VALUE of your account is:','${:.2f}'.format(futureValue))

def main():
    program_header()
    again = 'yes'
    while again == 'yes':
        presentVal, moInterest, numOfMonths = userInput()
        futureValue = calculate_futureValue(presentVal, moInterest, numOfMonths)
        output(futureValue)
        again = pyip.inputYesNo('Would you like to run another calculation? Yes or no: ')
        print()
    print()
    print('Thank you for using the Account Future Value Calculator.')

main()