def multiplication(a, b):
    c = 0
    counter = 0
    for j in range(1, b+1):
        for i in range(1, a+1):
            c = c +1
            counter = counter + 1
    print("The product is",c,"The number of iterations is",counter)
a = 6
b = 5
print("Using the second method", multiplication(a, b))