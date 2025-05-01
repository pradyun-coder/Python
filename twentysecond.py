import math
numA = input("Enter number")
numB = numA
binaryA = []
binaryB = []
for i in range (round(math.log2(int(numA))), -1, -1):
    if 2**i <= int(numA):
        binaryA.append(1)
        numA = int(numA) - 2**i
    else:
        binaryA.append(0)

for i in range (round(math.log2(int(numB))), -1, -1):
    if 2**i <= int(numB):
        binaryB.append(0)
        numB = int(numB) - 2**i
    else:
        binaryB.append(1)
if binaryA[0] == 0:
    binaryA.remove(0)
    binaryB.remove(1)

sumA = 0
for i in range(len(binaryA)-1, -1, -1):
    sumA = sumA + binaryA[i]*(2**i)
sumB = 0
for i in range(len(binaryB)-1, 0, -1):
    sumB = sumB + binaryB[i]*(2**i)
print(binaryA, sumA)
print(binaryB, sumB)