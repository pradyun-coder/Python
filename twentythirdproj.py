import math
numA = input("Enter number")
binaryA = []

for i in range (round(math.log2(int(numA))), -1, -1):
    if 2**i <= int(numA):
        binaryA.append(1)
        numA = int(numA) - 2**i
    else:
        binaryA.append(0)

if binaryA[0] == 0:
    binaryA.remove(0)

print(binaryA)
binaryA.reverse()

a = 0
for i in range(0, len(binaryA)):
    if binaryA[i] == 1 and a == 0:
        print(i +1)
        a = 1
        