number = 5
def summation(n):
    a = 0
    return n*(n+1)/2, a + 1
print("Using the first method", summation(number)) 

def secsummation(n):
    sum = 0
    a = 0
    for i in range(1, n+1):
        sum = sum + i
        a = a + 1
    return sum, a
print("Using the second method", secsummation(number))

def thirdsummation(n):
    sum = 0
    a = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum = sum + 1
            a = a + 1
    return sum, a
print("Using the third method", thirdsummation(number))

