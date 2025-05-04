def myfunction(n):
    countA = 0
    countB = 0
    countC = 0
    for i in range(0, n +1):
        countA += 1
    j = 1
    while(j<=n+1):
        j = j*2
        countB += 1
    for i in range(0, 100):
        countC += 1
    print(countA, countB, countC)
print(myfunction(5))