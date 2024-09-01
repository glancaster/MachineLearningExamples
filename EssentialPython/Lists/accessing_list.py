# list [start:stop:step]
l = list(range(10))
print(l[2:8:2]) # [2,4,6]

# slice objects
firstthree = slice(0,3)
print(l[firstthree])
