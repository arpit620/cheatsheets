import logging
import time

# https://www.youtube.com/watch?v=-ARI4Cz-awo
# Never have file name as 'logging.py'
# Levels : Debug, info, Warning, Error, Critical (# 10/20/30/40/50)
# Default level is "Warning"
# Default for logs is to print to console. So very similar to print statement

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.



# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='python/extras/test_basics.log', level=logging.DEBUG)

# Format
# https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(filename='python/extras/test_basics.log', level=logging.DEBUG,
                format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    time.sleep(1)
    logging.info("Inside add")
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logging.info("*"*10)