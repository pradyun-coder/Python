import math
numA = input("Enter number")
binaryA = []
instances = []
a = 0
b = 0
for i in range (round(math.log2(int(numA))), -1, -1):
    if 2**i <= int(numA):
        binaryA.append(1)
        numA = int(numA) - 2**i
    else:
        binaryA.append(0)
print(binaryA)
for i in binaryA:
    b = b + 1
    if i == 1:
        a = a + 1
    if i == 0:
        if binaryA[b-2] != 0:
            instances.append(a)
            a = 0
    elif b == len(binaryA) and i == 1:
        instances.append(a)
print(instances)
print(max(instances))