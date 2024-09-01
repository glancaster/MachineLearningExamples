names = ['Fred', 'Wilma','Barney']

def long_name(name):
    return len(name) > 5

filter(long_name,names) # ['Barney']
# or 
listcomp = [name for name in names if len(name) > 5]  # ['Barney']



from future_builtins import filter

filter(long_name,names) # <generator>
generator = ( name for name in names if len(name) > 5 )  # <generator> 
list(filter(long_name, names))  # ['Barney']
