for num in range(5):
    print(num)
else:
    print("out of nums")


for num in range(5):
    if num == 3:
        break
    else:
        print(num)
else:
    print("out of nums")



for num in range(5):
    if num == 3:
        continue
    else:
        print(num)
else:
    print("out of nums")

i = 0
while i < 5:
    print(i)
    i+=1
else:
    print('done')

i = 0
while i < 5:
    if i == 3:
        break
    else:
        print(i)
        i+=1
else:
    print('done')


