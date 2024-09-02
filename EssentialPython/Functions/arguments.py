# Positional Arguments
def func(*args):
    for i in args:
        print(i)
func(1,2,3)    
func(*[1,2,3])    
        
# Keyword Arguments
def kfunc(**kwargs):
    for name,value in kwargs.items():
        print(name,value)

kfunc(a=1,b=2,c=3)
kfunc(**{"a":1,"b":2, "c":3})

# Ordering of Arguments
#       |-positional-|-optional-|---keyword-only--|-optional-|
def func(arg1, arg2=10 , *args, kwarg1, kwarg2=2, **kwargs):
     pass
