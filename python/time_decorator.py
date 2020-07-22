import time

def time_usage(orig_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {:.2f} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


def my_timer(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval
    return wrapper

@time_usage
def func1():
    # print("Run time for func1:")
    time.sleep(1)

def main():
    func1()

if __name__ == "__main__":
    main()
