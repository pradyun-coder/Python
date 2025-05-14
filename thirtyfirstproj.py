def factorial(n, c=1):
    if n < 1:
        print(c)
        return
    b = n
    c = c*b
    b = n -1
    factorial(n-1, c)
number = input("Number for which the factorial needs to be calculated \n")
factorial(int(number))