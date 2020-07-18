
########################################################################
############################ First class functions #####################
########################################################################

def square(x):
    return x*x

f = square

# print(square)
# print(f)
# print(f(5))

#################

def cube(x):
    return x*x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1,2,3,4])
# print(squares)


#################

def logger(msg):
    def log_message():
        print("Log: ", msg)

    return log_message

log_hi = logger("Hi")
# log_hi()

#################

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Test Headline!')
# print_h1('Another Headline!')

# print_p = html_tag('p')
# print_p('Test Paragraph!')


########################################################################
############################ Closures #####################
########################################################################

# Access variables insdie the parent function

def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func

# print(outer_func)
# print(outer_func())
# print(outer_func()())

##############################

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func("hi")
hello_func = outer_func("hello")


hi_func()
hello_func()


#######################



import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

