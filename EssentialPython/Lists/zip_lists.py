alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b) # tuple

blist_longer = ['b1','b2','b3','b4']

# b4 is missing, zip iteration is on the shortest list
for a,b in zip(alist,blist_longer):
    print(a,b) # tuple
# nothing since empty list
for a,b in zip([],blist_longer):
    print(a,b) # tuple

clist = ['c1']
import itertools

for a,b,c in itertools.zip_longest(alist,blist_longer,clist):
    print(a,b,c)
