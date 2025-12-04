### FUNCTIONS ###

## def defines the function def some_function():
## Used to avoid duplicating code (easier to update)

# def hello():
#     # print three greetings
#     print('Good morning!')
#     print('Good afternoon!')
#     print('Good evening!')

# hello()
# hello()
# print('ONE MORE TIME!')
# hello()

##################################################################

### ARGUMENTS ###

# -- Arguments are entered in between the parentheses
# -- Parameters are variable that contain arguments (name in the below example)
# -- The lines after the function are called function calls

# def say_hello(name):
#     # Prints three greetings to the name provided
#     print('Good morning, ' + name)
#     print('Good afternoon, ' + name)
#     print('Good evening, ' + name)

# say_hello('Alice')
# say_hello('Bob')

## RETURN VALUES AND return STATEMENTS ###

# When creating a function using the def statement, you can specify the return value with a return statement which consists of:
# -- The return keyword
# -- The value or expression that the function should return

##################################################################

## RANDOM EIGHT BALL ##

# import random

# def get_answer(answer_number):
#     # Returns a fortune anser based on what int anser_number is, 1 to 9
#     if answer_number == 1:
#         return 'It is certain'
#     elif answer_number == 2:
#         return 'It is decidedly so'
#     elif answer_number == 3:
#         return 'Yes'
#     elif answer_number == 4:
#         return 'Reply hazy try again'
#     elif answer_number == 5:
#         return 'Ask again later'
#     elif answer_number == 6:
#         return 'Concentrate and ask again'
#     elif answer_number == 7:
#         return 'My reply is no'
#     elif answer_number == 8:
#         return 'Outlook not so good'
#     elif answer_number == 9:
#         return 'Very doubtful'
    
# print('Ask a yes or no question:')
# input('> ')
# r = random.randint(1, 9) ## YOU CAN SHORTEN THESE LAST THREE LINES TO -- print(get_answer(random.randint(1, 9))) --
# fortune = get_answer(r)
# print(fortune)

##################################################################

### The None value ###

# A value called None represents the absence of a value (null, nil or undefined in other languages)

##################################################################

### NAMED PARAMETERS ###

# Named parameters are optional parameters a function can take
# Ex. The print() function uses the optional parameters end and sep print('Hello', end = ' ') # end is defaulted to new line but in this example would just add a space
# sep adds a separator

##################################################################

### THE CALL STACK ###

# In a stack, items get added or removed from the top only, and the current topic is always at the top of the stack
# The call stack is how Python remembers where to return the execution after each function call
# The call stack is a section of your computer's memory that Python handles behind the scenes
# When your program calls a function, Python creates a frame object on top of the call stack.
# Frame objects store the line number of the original function call so that Python can remember where to return.
# When a function call returns, Python removes a frame object from the top of the stack and moves the exectution to the line number stored in it.


##### RESEARCH THE CALL STACK MORE ####### HARD TO GRASP ####

# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')

# def b():
#     print('b() starts')
#     c()
#     print('b() returns')

# def c():
#     print('c() starts')
#     print('c() returns')

# def d():
#     print('d() starts')
#     print('d() returns')

# a()

##################################################################

### LOCAL AND GLOBAL SCOPES ###

# Scope Rules #
# -- Code that is in the global scope, outside all functions, can't use local variables
# -- Code that is in one function's local scope can't use variables in any other local scope
# -- Code in a local scope can access global variables
# -- You can use the same name for different variables if they are in different scopes

## Code in global scope can't use local variables ##

# def spam():
#     eggs = 'sss'

# spam()
# print(eggs)

## Code in local scope can't use variables in other local scopes ##

# def spam():
#     eggs = 'SPAMSPAM'
#     bacon()
#     print(eggs) # Prints 'SPAMSPAM'

# def bacon():
#     ham = 'hamham'
#     eggs = 'BACONBACON'

# spam()

## Code in local scope can use global variables ##

# def spam():
#     print(eggs) # Prints 'GLOBALGLOBAL

# eggs = 'GLOBALGLOBAL'
# print(eggs)

## Local and global variables can have the same name ##

##### TRY NOT TO DO THIS ####

# def spam():
#     eggs = 'spam local'
#     print(eggs) # Prints 'spam local

# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # Prints 'bacon local'
#     spam()
#     print(eggs) # Prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs) # Prints 'global'

# -- If you need to modify a global variable from within a function use the global statement

# def spam():
#     global eggs
#     eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs) # Prints 'spam'

## Scope Identification ##
# Use these four rules to tell whether a variable is local scope or global scope:
# -- A variable in the global scope (outside all function) is always global
# -- A variable in a function with a global statement is always a global variable in that function
# -- If a variable is assigned in a function it is local
# -- If the function uses a variable but never assigned it is global

# OFTEN ALL YOU NEED TO KNOW ABOUT A FUNCTION ARE ITS INPUTS AND ITS OUTPUT VALUE

##################################################################

### EXCEPTION HANDLING ###

# You want the program to detect erros, handle them, and then continue to run

# def spam(divide_by):
#     return 42 / divide_by

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# Errors can be handled with try and except statements

# def spam(divide_by):
#     try:
#         # The code in this block that causes ZeroDivisionError won't crash the program:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         # If ZeroDivisionError happened, the code in this block runs:
#         print('Error: Invalid argument.')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

##################################################################

### ZIGZAG ###

# import time, sys
# indent = 0 # How many spaces to indent
# indent_increasing = True # Whether the indentation is increasing or not

# try:
#     while True: # The main program loop
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10th of a second

#         if indent_increasing:
#             # Increase the number of spaces
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction
#                 indent_increasing = False
#         else:
#             # Decrease the number of spaces
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()

##################################################################

### SPIKE ###

# import time, sys

# try:
#     while True: # The main program loop
#         # Draw lines with increasint length
#         for i in range(1, 9):
#             print('-' * (i * i))
#             time.sleep(0.1)

#         # Draw lines with decreasing length
#         for i in range(7, 1, -1):
#             print('-' * (i * i))
#             time.sleep(0.1)
# except KeyboardInterrupt:
#     sys.exit()\

##################################################################

#### PRACTICE QUESTIONS ####

# 1.  Why are functions advantageous to have in your programs?
#   2.  When does the code in a function execute: when the function is defined or when the function is called?
#   3.  What statement creates a function?
#   4.  What is the difference between a function and a function call?
#   5.  How many global scopes are there in a Python program? How many local scopes are there?
#   6.  What happens to variables in a local scope when the function call returns?
#   7.  What is a return value? Can a return value be part of an expression?
#   8.  If a function does not have a return statement, what is the return value of a call to that function?
#   9.  How can you force a variable in a function to refer to the global variable?
# 10.  What is the data type of None?
# 11.  What does the import areallyourpetsnamederic statement do?
# 12.  If you had a function named bacon() in a module named spam, how would you call it after importing spam?
# 13.  How can you prevent a program from crashing when it gets an error?
# 14.  What goes in the try clause? What goes in the except clause?
# 15.  Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?

#### PRACTICE PROGRAM ####

# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
# Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer; sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value. To make the output more compact, the print() calls that print the numbers should have a sep=' ' named parameter to print all values on one line.
# The output of this program could look something like this:

# Enter number:
# 3
# 3 10 5 16 8 4 2 1

# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

# Input Validation
# Add try and except statements to the previous project to detect whether the user entered a non-integer string. Normally, the int() function will raise a ValueError error if it is passed a non-integer string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.