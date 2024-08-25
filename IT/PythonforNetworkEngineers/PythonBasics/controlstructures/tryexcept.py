try:
    print("lets divide by 0")
    2/0
    print("math is cool")
except ZeroDivisionError:
    print("You can't divide by 0")
try:
    print("lets divide by 0")
    2/int("r")
    print("math is cool")
except ValueError:
    print("You can't divide by strings")
try:
    print("lets divide by 0")
    2/int("0")
    print("math is cool")
except( ValueError, ZeroDivisionError):
    print("you did something dumb")
try:
    print("lets return something if it worked")
    res = 2/int("4")
    print("math is cool")
except( ValueError, ZeroDivisionError):
    print("you did something dumb")
else:
    print(f"result: {res}")
try:
    print("lets return something if it worked")
    res = 2/int("4")
    print("math is cool")
except( ValueError, ZeroDivisionError):
    print("you did something dumb")
else:
    print(f"result: {res}")
finally:
    print("we made it, thank goodness")




# same functionality different structure
while True:
    a = "5"
    b = "1"
    try:
        res = int(a)/int(b)
    except ValueError:
        print("only digits dude")
    except ZeroDivisionError:
        print("can't divide by zero dude")
    else:
        print(res)
        break

while True:
    a = "5"
    b = "1"
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("can't divide by zero dude")
        else:
            print(int(a)/int(b))
            break

    else:
        pxint("only digits dude")
        
            

