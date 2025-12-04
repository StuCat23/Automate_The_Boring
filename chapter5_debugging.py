### RAISING EXCEPTIONS ###

# The raise keyword
# A call to the Exception() function
# A string with a helpful error message passed to the Exception() function

# def box_print(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
    
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# try:
#     box_print('*', 4, 4)
#     box_print('0', 20, 5)
#     box_print('x', 1, 3)
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An exception happned: ' + str(err))
# try:
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An exception happened: ' + str(err))

##################################################################

### Assertions ###

# The assert keyword
# A condition (that is, an expression that evaluates to True or False)
# A comma
# A string to display when the condition is False

# Assertions are for programmer errors, not user errors (used during development)

### Logging ###

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start the program')

# def factorial(n):
#     logging.debug('Start of factorial(' + str(n) + ')')
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total

# print(factorial(5))
# logging.debug('End of program')

## Logging Levels in Python ##

# It is up to you to decide which category you log message falls into.

# DEBUG -- logging.debug() -- Lowest level, used for small detailer. Usually care about these messages only when diagnosing problems.
# INFO -- logging.info() -- Used to record information about general events in your program or to confirm that it's working at various points.
# WARNING -- logging.warning() -- Used to indicate a potential problem that doesn't prevent the program from working but might later.
# ERROR -- logging.error() -- Used to record at error that caused the program to fail to do something.
# CRITICAL -- logging.critical() -- The highest level, used to indicate a fatal error that has caused, or is about to cause, the program to stop running entirely.

# Disabled Logging
# logging.disable() disables the log messages so you don't have to remove the logging calls by hand