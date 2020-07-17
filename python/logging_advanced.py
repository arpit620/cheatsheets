import logging
import time
import log_employee_adv

# Importing other module with logging info takes over below config.
# Logging config doesn't get overwritten
# Replace `logging` with new logger name.
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Logging-Advanced

# Format
# https://docs.python.org/3/library/logging.html#logrecord-attributes

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('python/extras/test_basics.log')
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    time.sleep(1)
    logger.info("Inside add")
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        # To capture Traceback use keyword 'exception'
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logger.info("*"*10)