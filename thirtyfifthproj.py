def myfunction1(n, a):
    if (n>0):
        print(a)
        print("end")
        return
    for i in range(0, int(n) +1):
        a = a +1
    myfunction1(n/2, a)
    myfunction1(n/3, a)
def myfunction2(n, a):
    if (n<= 1):
        print(a)
        print("end")
        return
    a = a +1
    myfunction2(n-1, a)

myfunction1(10, 0)
myfunction2(10, 0)