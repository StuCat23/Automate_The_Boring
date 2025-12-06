### The Dictionary Data Type ###

# A dictionary is a mutable collection of many values
# Unlike indexes for lists, indexes for ditionaries can use many different data types, not just integers
# Dictionary indexes are called keys and a key with its associated value is called a key-value pair
# A dictionary is entered between curly brackets {}
# You can store multiple pieces of data about the same thing in a single variable

## Comparing Dictionaries and Lists ##

# Unlike lists, items in dictionaries are unordered

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday info for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

### Returning Keys and Values ##

# Three dictionary methods will return list-like values of the dictionary's keys, values or both
# 1. keys()
# 2. values()
# 3. items()
# These can be used in for loops but can't be modified

# If you want to get an actual list from one of the above methods pass its list-like return value to the list() function
# list(spam.keys())

## Checking whether a Key Exists ##

# Dictionaries have a get() method that takes two arguments:
# 1. The key of the value to retrieve
# 2. A fallback value to return if that key doesnt exit

# picnic_items = {'apples': 5, 'cups': 2}
# 'I am bringin ' + str(picnic_items.get('cups', 0)) + ' cups.'
# >> 'I am bringing 2 cups.'
# 'I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.'
# >> 'I am bring 0 eggs.' # Since there is no 'eggs' key in picnic_items dictionary, the get() method returns the dafault fallback value.

## Setting Default Values ##

# You'll often have to set a value in a dictionary for a certain key only if that key doesn't already have a value.
# setdefault() - nice shortcut to ensure a key exists

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# print(count)

####################################################

## Model Real-World Things Using Data Structures ##

## Chess Board ##

# import sys, copy

# STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
# 'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
# 'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
# 'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
# 'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
# 'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

# BOARD_TEMPLATE = """
#     a    b    c    d    e    f    g    h
#    ____ ____ ____ ____ ____ ____ ____ ____
#   ||||||    ||||||    ||||||    ||||||    |
# 8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
#   ||||||    ||||||    ||||||    ||||||    |
# 2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
#   ||||||____||||||____||||||____||||||____|
#   |    ||||||    ||||||    ||||||    ||||||
# 1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
#   |____||||||____||||||____||||||____||||||
# """
# WHITE_SQUARE = '||'
# BLACK_SQUARE = '  '

# # Step 3: Print the Current Chessboard

# def print_chessboard(board):
#     squares = []
#     is_white_square = True
#     for y in '87654321':
#         for x in 'abcdefgh':
#             print(x, y, is_white_square)