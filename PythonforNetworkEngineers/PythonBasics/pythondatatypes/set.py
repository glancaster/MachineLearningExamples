# Set
i = 1

l1 = [56,87,524,789]
s1 = set(l1)

print(f"{i}:", s1);i+=1

print('set methods')

s1.add(45)
print(f"{i}:", s1);i+=1

s1.discard(21) # no error
print(f"{i}:", s1);i+=1
s1.discard(524)
print(f"{i}:", s1);i+=1

s1.clear()
print(f"{i}:", s1);i+=1

print('set operations')

s2 = {35,45,55,65}
s3 = {15,25,35,55}

print(f"{i}:", s2.union(s3));i+=1
print(f"{i}:", s2 | s3 );i+=1

print(f"{i}:", s2.intersection(s3));i+=1
print(f"{i}:", s2 & s3);i+=1

print('set creation')

s4 = {}
print(f"{i}:", type(s4));i+=1

s5 = set()
print(f"{i}:", type(s5));i+=1

s6 = set('long long message')
print(f"{i}:", s6);i+=1

s7 = set([1,1,5,8,4,5,5,2])
print(f"{i}:", s7);i+=1




 
