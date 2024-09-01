a = [1,2,3,4,5]

# append adds one new element whatever that may be
a.append(6)
a.append([7,8])
a.append("9 10")

print(f"{a=}")

a = [1,2,3,4,5]
b = [6,7,8]

# extend adds each element to the end of the list
a.extend(b)
a.extend(range(3))

print(f"{a=}")

# index finds index of value, starting index can be given 
a = [1,2,3,4,5]
a.index(3) # 2
# a.index(19) # error
# a.index(3,3) # error

print(f"{a=}")
# pop removes and returns last element, index to pop can be given
a = [1,2,3,4,5]
a.pop() # 5 , a = [1,2,3,4]
a.pop(1) # 2 , a = [1,3,4]

print(f"{a=}")
# remove removes value if in list else error
a.remove(3) # a = [1,4]

print(f"{a=}")
# reverse
a.reverse() # a = [4,1]

print(f"{a=}")
# count 
a = [1,2,2,3,3,4,4,5,6,6,6]
a.count(6) # 3

print(f"{a=}")
# sort sorts in numerical or lexicographical order
a = [2,5,6,4,1]
a.sort() # a = [1,2,4,5,6]

print(f"{a=}")
# sort can sort by attributes
import datetime

l = [{'name':'John Cena', 'birthday': datetime.date(1992, 9, 12),'size': {'height': 175, 'weight': 100}},
 {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),'size' : {'height': 180, 'weight': 90}},
 {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'size': {'height': 185, 'weight': 110}}]

l.sort(key=lambda item: item['size']['height'])
# l: [John Cena, Chuck Norris, Jon Skeet]

print(f"{l=}")

from operator import itemgetter,attrgetter

people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')

people.sort(key=by_age) #in-place sorting by age
people.sort(key=by_salary) #in-place sorting by salary

print(f"{people=}")

# attrgetter also available to sort for attributes like in a class

# clear

a = [1,2,3,4,5]
a.clear() # a = []

# replication
a = [1,2,4]*5
print(f"{a=}")

# element deletion
a = list(range(10))
del a[::2] # [1,3,5,7,9]
del a[-1] # [1,3,5,7]
del a[:] # []

# copying 
a = list(range(5))
b = a 
a.append(5)
# b = [1,2,3,4,5] # this is same list as a

# to copy correctly
b = a[:]
b2 = list(a)

import copy
b3 = copy.copy(a) # for references
b4 = copy.deepcopy(a) # for objects
