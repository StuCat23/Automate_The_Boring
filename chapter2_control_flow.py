# username = 'Mary'
# password = 'swordfish'

# if username == 'Mary':
#     print('Hello, Mary')
#     if password == 'swordfish':
#         print('Acess granted.')
#     else:
#         print('Wrong password')

# name = 'Stu'

# if name == 'Alice':
#     print('Hi, Alice.')
# else:
#     print('Hello, Stranger.')

# name = 'Alice'
# age = 33

# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')

# name = 'Carol'
# age = 3000

# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif (age > 2000):
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif (age > 100):
#     print('You are not Alice, grannie.')

# name = 'Carol'
# age = 3000

# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# else:
#     print('You are neither Alice nor a little kid.')

################################################################

### OPPOSITE DAY ###

# today_is_opposite_day = True

# # Set say_it_is_opposite_day based on today_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day = True
# else:
#     say_it_is_opposite_day = False

# # If it is opposite day, toggle say_it_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day == True

# # Say what day it is:
# if say_it_is_opposite_day == True:
#     print('Today is Opposite Day.')
# else:
#     print('Today is not Opposite Day.')

################################################################

### DISHONEST CAPACITY CALCULATOR ###

# print('Enter TB or GB for the advertised unit:')
# unit = input('>')

# # Calculate the amount that the advertised capacity lies:
# if unit == 'TB' or unit == 'tb':
#     discrepancy = 1000000000000 / 1099511627776
# elif unit == 'GB' or unit == 'gb':
#     discrepancy = 1000000000 / 1073741824
# else:
#     print('You must enter TB or GB')

# print('Enter the advertised capacity:')
# advertised_capacity = input('>')
# advertised_capacity = float(advertised_capacity)

# # Calculate the real capacity, round it to the neares hundreths, and convert it to a string so it can be concatenated
# real_capacity = str(round(advertised_capacity * discrepancy, 2))

# print('The actual capacity is ' + real_capacity + '' + unit)

################################################################

### PRACTICE ###

# spam = 3

# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings!')