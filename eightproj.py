def iter(n):
    iteration = 0
    for i in range(1, n + 1):
        for j in range(1, n +2):
            print("*", end = " ")
            iteration += 1
        print("")
    print("when n is ", n, " Iteration = ", iteration) 

number = int(input("Enter number \n"))
iter(number)

def iter(n):
    iteration = 0
    print("The number input by user is "+ n)
    iteration += 1
    print("The number of iterations", iteration)
number = input("Enter number \n")