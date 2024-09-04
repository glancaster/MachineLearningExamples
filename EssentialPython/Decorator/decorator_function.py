def secret_function(f):
    return f

@secret_function
def function():
    print("function")

# same as secret_function(function)

def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func

@print_args
def multiply(a,b):
    return a*b

print(multiply(3,5))


# useful snippet - timeit
import time
def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print("Took {} seconds".format(t2-t1))
        return f
    return inner

@timer
def example():
    for n in range(89898989):
        pass
example()
