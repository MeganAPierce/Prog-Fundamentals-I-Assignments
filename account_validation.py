# Megan Pierce                      Oct 13, 2021
# Charge Account Validation V1      Ch 7, Problem 5
#
#
# Using charge_accounts.txt file, write a program that reads the contents of the file
# into a list. The program should then ask the user to enter a charge account number
# (7 DIGITS). If the number is in the list the program should display a message indicating the
# number is valid.

import pyinputplus as pyip

def UserAccountNum():
    userAccount = pyip.inputInt('Please enter your account number: ')
    userAccount = str(userAccount)
    while len(userAccount) != 7:
        print()
        userAccount = pyip.inputInt('Account numbers contain 7 digits. Please double check'
                                         ' and try entering your account number again: ')
        userAccount = str(userAccount)
    return str(userAccount)

def ListFile():
    #create a list from the charge_accounts.txt
    list = []
    Accounts = open('charge_accounts.txt','r')
    for line in Accounts:
        #remove \n
        line = line.rstrip('\n')
        list.append(line)
    Accounts.close()
    return list

def Validate(userAccount,list):
    #check for user input in the list created in ListFile()
    if userAccount in list:
        print()
        print('Search successful. Account number is valid.')
    else:
        print()
        print('Search unsuccessful. Account number does not exist.')

def main():
    print()
    print('{:^43}'.format('CHARGE ACCOUNT VALIDATION'))
    print('')
    userAccount = UserAccountNum()
    list = ListFile()
    Validate(userAccount,list)

main()

