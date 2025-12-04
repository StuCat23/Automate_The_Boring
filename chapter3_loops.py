### WHILE LOOPS ###
# Make a block of code execute over and over again
# The code in the while clause will be executed as long as the statement's condition is True
# A while statement always consists of the following:
# -- The While keyword
# -- A condition
# -- A colon
# -- Starting on the next line, an indented block of code (called the while clause or while block)

## EXAMPLE ##
# While loop keeps going until false

# spam = 0

# while spam < 5:
#     print('Hello, World.')
#     spam = spam + 1

#############################################################

### AN ANNOYING WHILE LOOP ###

# name = ''

# while name != 'your name':
#     print('Please type your name.')
#     name = input('>')
# print('Thank you!')

#############################################################

### BREAK STATEMENTS ###
# Breaks out of loop clause early

# while True:
#     print('Please type your name.')
#     name = input('>')
#     if name == 'your name':
#         break
# print('Thank you!')

#############################################################

### CONTINUE STATEMENTS ###
# When program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevalutes the loop's condition

# while True:
#     print('Who are you?')
#     name = input('>')
#     if name != 'Joe':
#         continue
#     print('Hello, Joe, What is the password? (It is a fish.)')
#     password = input('>')
#     if password == 'swordfish':
#         break
# print('Access granted.')

#############################################################

### for LOOPS AND THE range() FUNCTION ###
# A for statement looks something like for i in range(5): and includes the following:
# -- The for keyword
# -- A variable name
# -- The in keyword
# -- A call to the range() function with up to three integers passed to it
# -- A colon
# -- Starting on the next line, an indented block of code (called the for clause or for block)

# print('Hello!')
# for i in range(5):
#     print('On this iteration , i is set to ' + str(i))
# print('Goodbye!')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

## This is the same using a while loop
# print('Hello')
# i = 0
# while i < 5:
#     print('On this iteration, i is set to ' + str(i))
#     i = i + 1
# print('Goodbye!')

### Arguments to range() ###
# for i in range(12, 16): # The first argument is where the for loop's variable starts and second argument will be up to but not including, the number to stop at.
#     print(i)

# for i in range(0, 10, 2): # The third argument is the step argument. The step is the amount by which the variable is increased after each iteration.
#     print(i)

# for i in range(5, -1, -1): # This would step down instead of up
#     print(i)

#############################################################

### IMPORTING MODULES ###
# Python comes with a set of modules called the standard library. (Ex. math module has mathematics-related functions, random module has random number-related functions, etc.)
# Befor you can use the functions in a module you must import the module with an import statement.
# An import statement consists of the following:
# -- The import keyword
# -- The name of the module
# -- Optionally, more module names, as long as they are separated by commas

# import random

# for i in range(5):
#     print(random.randint(1, 10))

# DON'T USE THE NAMES OF ANY BUILT-IN PYTHON FUNCTIONS FOR YOUR SCRIPT, FILE OR VARIABLE NAMES #

# Ending a Program Early with sys.exit()

# import sys

# while True:
#     print('Type exit to exit.')
#     response = input('> ')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')


 ## GUESS THE NUMBER ##

# This is a guess the number game.
# import random

# secret_number = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# # Ask the player to guess 6 times
# for guesses_taken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input('>'))

#     if guess < secret_number:
#         print('Your guess is too low!')
#     elif guess > secret_number:
#         print('Your guess is too high!')
#     else:
#         break # This condition is the correct guess!

# if guess == secret_number:
#     print('Good job! Yout got it in ' + str(guesses_taken) + ' guesses!')
# else:
#     print('Nope. The number was ' + str(secret_number))

## ROCK PAPER SCISSORS

# import random, sys

# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0

# while True: # The main game loop
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties) )
#     while True: # The player input loop
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         player_move = input('> ')
#         if player_move == 'q':
#             sys.exit() # Quit program
#         if player_move == 'r' or player_move == 'p' or player_move == 's':
#             break # Break out of the player input loop
#         print('Type one of r, p, s, or q.')

#     # Display what the player chose:
#     if player_move == 'r':
#         print('ROCK versus...')
#     elif player_move == 'p':
#         print('PAPER versus...')
#     elif player_move == 's':
#         print('SCISSORS versus...')

#     # Display what the computer chose:
#     move_number = random.randint(1,3)
#     if move_number == 1:
#         computer_move = 'r'
#         print('ROCK')
#     elif move_number == 2:
#         computer_move = 'p'
#         print('PAPER')
#     elif move_number == 3:
#         computer_move = 's'
#         print('SCISSORS')

#     # Display and record the win/loss/tie:
#     if player_move == computer_move:
#         print('It is a tie!')
#         ties = ties + 1
#     elif player_move == 'r' and computer_move == 's':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'p' and computer_move == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 's' and computer_move == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'r' and computer_move == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 'p' and computer_move == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif player_move == 's' and computer_move == 'r':
#         print('You lose!')
#         losses = losses + 1