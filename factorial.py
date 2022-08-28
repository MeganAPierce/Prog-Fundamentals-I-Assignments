# Megan A Pierce                 Sept 21, 2021
# Factorial Calculation V.1      Exercise 4.12
#
#
# Write a program that lets the user enter a non negative integer then uses
# a loop to calculate the factorial of that number. Display that factorial.

#Welcome statement
print()
print('{:^78}'.format('FACTORIAL PROGRAM'))
print()
print("When given a nonnegative integer, this program will calculate it's factorial.")
print()

#input
number = int(input('Please enter a positive number: '))
one = 1 #variable to help determine if input is valid
#input validation
while number < one:
    print('That number is negative. Please enter a positive number: ')
    print()

#for valid input, calculation:

multiplyer = 1  #factorials you start with 1 (ex: 7! = 1x2x3x4x5x6x7)

for factorial in range(1, (number + 1)):
    multiplyer = multiplyer * factorial
    #Made a dumb mistake first time:
    #Don't put your print statement here or you're going to see it "number" times.

print('Factorial of', number,'=', '{:,}'.format(multiplyer))

#End Statment
print()
print('Factorial calculation complete.')