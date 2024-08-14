# types conversion
i = 1

print(f"{i}:", int('10'));i+=1
print(f"{i}:", int('111',2));i+=1
print(f"{i}:", bin(10));i+=1
print(f"{i}:", bin(7));i+=1
print(f"{i}:", hex(10));i+=1
print(f"{i}:", hex(63));i+=1
print(f"{i}:", list('message'));i+=1
print(f"{i}:", list({1,5,4}));i+=1
print(f"{i}:", list((1,5,4)));i+=1
print(f"{i}:", set([1,5,4]));i+=1
print(f"{i}:", set((1,5,4)));i+=1
print(f"{i}:", set('message'));i+=1
print(f"{i}:", tuple([1,5,4]));i+=1
print(f"{i}:", tuple({1,5,4}));i+=1
print(f"{i}:", tuple('message'));i+=1
print(f"{i}:", str(108));i+=1



