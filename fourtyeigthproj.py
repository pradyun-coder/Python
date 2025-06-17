def checker(number):
    if number < 0:
        return
    a = input("enter number")
    checker(int(a))

b = input("Enter number")
checker(int(b))