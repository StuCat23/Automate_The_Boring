### LISTS ### Like arrays in JS

# The List Data Type #
# A list is a value that contains multiple values in an ordered sequence (Ex. ['cat', 'bat', 'rat', 'elephant'] )
# The term list value refers to the list itself
# You can have multiple lists in a value (ex. spam = [['cat', 'bat'], [10, 20, 30, 40, 50]] )
# Indexes are found using list name[1]

##################################################################

## Slices ##
# A slice can get several values from a list (ex. spam[1:4] the first integer is where the slice starts and the second is where the slice ends(will not include the ending index))
# You can leave out one or both of the indexes on either side of the colon in a slice

## The len() function ##
# Returns the number of values in a list value passed to it

##################################################################

## Value Updates ##
# You can use an index of a list to change the value at that index

##################################################################

## Concatenation and Replication ##
# You can concatenate and replicate lists with the + and * operators, just like you would with strings

##################################################################

## del Statements ##
# The del statement will delete values at an index in a list. All of the values in the list after the deleted value will move up one index.

##################################################################

### Working with Lists ###

# cat_names = []

# while True:
#     print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop.): ')
#     name = input()
#     if name == '':
#         break
#     cat_names = cat_names + [name] # List concatenation
# print('The cat names are: ')
# for name in cat_names:
#     print(' ' + name)

##################################################################

## for Loops and Lists ##

# ** Run this is terminal ** #
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ', + str(i) + ' in supplies is: ' + supplies[i])

##################################################################

## The in and not in Operators
# You can determine whether a value is or isn't in a list with the in and not in operators.

# my_pets = ['Zohie', 'Pooka', 'Fat-tail']
# print('Enter a pet name: ')

# name = input()
# if name not in my_pets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

##################################################################

## The Multiple Assignment Trick ##

# The multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign mulitiple variables with the values in a list in one line of code.

# # Instead of doing:
# cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# dispostion = cat[2]

# # You could use:
# cat = ['fat', 'gray', 'loud']
# size, color, disposition = cat

##################################################################

## List Item Enumeration ##

# Instead of using range(len(some_list)) with a for loop to obtain the integer index of the item in the list, you can call enumerate().
# This is helpful when you need both the item and the item's index in the loop's block

##################################################################

## Random Selection and Ordering ##

# The random module has a couple of functions that accept lists for arguments. The random.choice() function will return a randomly selected item from the list.
# Refer to documentation

##################################################################

## Augmented Assignment Operators ##

# +=
# -+
# *=
# /=
# %=

##################################################################

## Methods ##

# Finding Values #
# .index()

# Adding Values #
# .append() -- Adds the argument to the end of the list
# .insert() -- Inserts a value at any index in the list

# Removing Values #
# .remove() -- Accepts a value to remove from the list on which it's called -- Will only remove the first instance if the value is listed multiple times
# The del statement is useful when you know the index of the value you want to remove, while .remove() is useful when you know the value

# Sorting Values #
# .sort() -- Sorts lists in numerical order (also applies to strings)
# .sort(reverse=True) -- Sorts in reverse order
# Sorts the list in place; don't try to capture the return value by writing spam = spam.sort()
# You can't sort lists that have number values and string values in them
# .sort() uses ASCIIbetical order -- Uppercase letters come before lowercase letters -- If you need to sort values in regular alphabetical order pass str.lower for the key keyword
# spam.sort((key=str.lower))

# Reversing Values #
# .reverse() -- used to quickly reverse the order of the items in a list.

##################################################################

## Magic 8 Ball with a List ##

# import random

# messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']

# print('Ask a yes or no question: ')
# input('> ')
# print(messages[random.randint(0, len(messages) - 1)])

##################################################################

## Sequence Data Types ##

##################################################################

## Tuple Data Type ##

# Two differences from list data type
# 1. You write tuples with () ex. eggs = ('hello', 42, 0.5)
# 2. They are immutable

# If you only have one value in your tuple, you can indicate this by adding a trailing comma after the value inside the ()
# Convertin a tuple to a list is handy if you need a mutable version of the tuple value.

##################################################################

## Arguments ##

# def eggs(some_parameter):
#     some_parameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

##################################################################

## copy() and deepcopy() Functions ##

# When you do not want to change the original list

##################################################################

## The Matrix Screensaver ##

# import random, sys, time

# WIDTH = 70 # The number of columns

# try:
#     # For each column, when the counter is 0, no stream is shown.
#     # Otherwise, it acts as a counter for how many times a 1 or 0 should be displayed in that column
#     columns = [0] * WIDTH
#     while True:
#         # Loop over each column
#         for i in range(WIDTH):
#             if random.random() < 0.02:
#                 # Restart a stream counter on this column
#                 # The stream length is between 4 and 14 character long
#                 columns[i] = random.randint(4, 14)

#             # Print a character in this column:
#             if columns[i] == 0:
#                 # Change this ' '' to '.' to see the empty spaces:
#                 print(' ', end='')
#             else:
#                 # Print a 0 or 1:
#                 print(random.choice([0, 1]), end='')
#                 columns[i] -= 1 # Decrement the counter for this columnn
#         print() # Prints a newline at the end of the row of columns
#         time.sleep(0.1) # Each row pauses for one tenth of a second
# except KeyboardInterrupt:
#     sys.exit() # When Ctrl-C is pressed, end the program

##################################################################

# Practice Questions

#   1.  What is []?

#   2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

# For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

#   3.  What does spam[int(int('3' * 2) // 11)] evaluate to?

#   4.  What does spam[-1] evaluate to?

#   5.  What does spam[:2] evaluate to?

# For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

#   6.  What does bacon.index('cat') evaluate to?

#   7.  What does bacon.append(99) make the list value in bacon look like?

#   8.  What does bacon.remove('cat') make the list value in bacon look like?

#   9.  What are the operators for list concatenation and list replication?

# 10.  What is the difference between the append() and insert() list methods?

# 11.  What are two ways to remove values from a list?

# 12.  Name a few ways that list values are similar to string values.

# 13.  What is the difference between lists and tuples?

# 14.  How do you write the tuple value that has just the integer value 42 in it?

# 15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?

# 16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

# 17.  What is the difference between copy.copy() and copy.deepcopy()?

##################################################################

# Practice Programs

# For practice, write programs to do the following tasks.

# Comma Code

# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# Coin Flip Streaks

# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an H for each heads and a T for each tails, you’ll create a list that looks like T T T T H H H H T T. If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating heads-tails results like H T H T H H T H T T—which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

# You can start with the following template:

# import random
# number_of_streaks = 0
# for experiment_number in range(10000):  # Run 100,000 experiments total.
#     # Code that creates a list of 100 'heads' or 'tails' values

#     # Code that checks if there is a streak of 6 heads or tails in a row

# print('Chance of streak: %s%%' % (number_of_streaks / 100))
# Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

# To create a list, use a for loop that appends a randomly selected 'H' or 'T' to a list 100 times. To determine if there is a streak of six heads or six tails, create a slice like some_list[i:i + 6] (which contains the six items starting at index i) and then compare it to the list values ['H', 'H', 'H', 'H', 'H', 'H'] and ['T', 'T', 'T', 'T', 'T', 'T'].