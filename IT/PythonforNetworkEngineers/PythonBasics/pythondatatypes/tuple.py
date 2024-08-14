# tuple
i = 1

t1 = tuple()
print(f"{i}:", t1);i+=1

t2 = ('secret',)
print(f"{i}:", t2);i+=1

l1 = ['hi', 'from', 'the', 'big', 'apple']
t3 = tuple(l1)
print(f"{i}:", t3);i+=1

print(f"{i}:", t3[0]);i+=1
# t3[0] = 'hello' -> error

print(f"{i}:", sorted(t3));i+=1



