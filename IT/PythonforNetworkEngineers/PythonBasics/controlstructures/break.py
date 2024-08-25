for num in range(10):
    if num < 7:
        print(num)
    else:
        break

i = 0
while i < 10:
    if i == 5:
        break
    else:
        print(i)
        i+=1


user = input("Enter user: ")
password = input("Enter password: ")


while True:
    if len(password) < 8:
        print("Password too short\n")
    elif user in password:
        print("Password contains username\n")
    else:
        print("Password for user {} is set".format(user))
        break
    
    password = input("Enter password: ")
