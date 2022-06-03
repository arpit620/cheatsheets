# Official documentation
# https://docs.python.org/3/library/timeit.html

# importing the required module
from audioop import add
import timeit

from sklearn.metrics import explained_variance_score
 
# code snippet to be executed only once
mysetup = "from math import sqrt"
 
# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
 
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))


#####################################################


# importing the required modules
import timeit

# if a = 5:
#     b = 5
#     el
 
# binary search function
def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist))//2
        if mylist[mid] == find:
            return True
        elif mylist[mid] < find:
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
    return False
 
 
# linear search function
def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False
 
 
# compute binary search time
def binary_time():
    SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''
 
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
 
    # printing minimum exec. time
    print('Binary search time: {}'.format(min(times)))       
 
 
# compute linear search time
def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''
     
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
 
    # printing minimum exec. time
    print('Linear search time: {}'.format(min(times))) 
 
if __name__ == "__main__":
    linear_time()
    binary_time()
    
#####################################################

# Globals can also be used: 

def myfunc():
    for x in range(100_000):
        pass
    
print(timeit.timeit(stmt='myfunc()', setup='', globals=globals()))

print(timeit.timeit(stmt='x=0; y=0', setup='', number=1000))

#####################################################

# These magic functions runs only for default amount of time. 
# So if we pass easy function it will run more iterations as compared to complex function.

# Line Magic function in ipython

%timeit for _ in range(1000): True
%timeit for _ in xrange(1000): True

def add2nums(a,b):
    return a+b

%timeit add2nums(3,1)

%timeit a = [4 + i for i in range(1000)]


# Cell Magic

%%timeit

a = []
for i in range(1000):
    a.append(4+i)
    

# Numpy can add huge boost to logics if used right.

        
########################################################################

# Explore 

print min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000))

