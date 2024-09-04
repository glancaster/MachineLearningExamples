# singleton restricts instantiation of a class to one instance or object

def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None: 
            instance[0] = cls(*args,**kwargs)
        return instance[0]
    return wrapper

@singleton
class SomeSingletonClass:
    x = 2
    def __init__(self):
        print("created")

instance = SomeSingletonClass()
instance = SomeSingletonClass()
print(instance.x)

instance.x = 3
print(SomeSingletonClass().x)
