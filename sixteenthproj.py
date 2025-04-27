#setup
import math

numA = input("Enter number")
numB = input("Enter number")
binaryA = []
binaryB = []
for i in range (round(math.log2(int(numA))), -1, -1):
    if 2**i <= int(numA):
        binaryA.append("1")
        numA = int(numA) - 2**i
    else:
        binaryA.append("0")

for i in range (round(math.log2(int(numB))), -1, -1):
    if 2**i <= int(numB):
        binaryB.append("1")
        numB = int(numB) - 2**i
    else:
        binaryB.append("0")

if len(binaryB) >= len(binaryA):
    minimum = binaryA
    maximum = binaryB
else:
    minimum = binaryB
    maximum = binaryA
print(minimum)
print(maximum)

#AND operator
sum = []
minimum.reverse()
maximum.reverse()

for i in range (0, len(minimum)):
    if minimum[i] == '0' or maximum[i] == '0':
        sum.append(0)
    elif minimum[i] == '1' and maximum[i] == '1':
        sum.append(1)

b = 0
count = -1
print(sum)
for i in sum:
    count = count + 1
    number = sum[count]
    a = number*(count+1)
    b = b + a
print(b)
