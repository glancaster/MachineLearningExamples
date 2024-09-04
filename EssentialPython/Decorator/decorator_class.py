class Decorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self,*args, **kwargs):
        print("before")
        res = self.func(*args,**kwargs)
        print("after")
        return res

@Decorator
def testfunc():
    print("inside")

testfunc()
