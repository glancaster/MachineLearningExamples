a = 5
while a > 0:
    print(a)
    a-=1 

user = input("Enter user: ")
password = input("Enter password: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Password too short\n")
        password = input("Enter password: ")
    elif user in password:
        print("Password contains username\n")
        password = input("Enter password: ")
    else:
        print("Password for user {} is set".format(user))
        password_correct = True

