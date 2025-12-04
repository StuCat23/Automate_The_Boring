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

