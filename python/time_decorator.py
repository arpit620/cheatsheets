import time

def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval
    return wrapper

@time_usage
def func1():
    print("Run time for func1:")
    time.sleep(2)

def main():
    func1()

if __name__ == "__main__":
    main()
