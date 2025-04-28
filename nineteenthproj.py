import math
binaryA = []
numA = input("Enter number")

for i in range (round(math.log2(int(numA))), -1, -1):
    if 2**i <= int(numA):
        binaryA.append(1)
        numA = int(numA) - 2**i
    else:
        binaryA.append(0)
print(binaryA)
zeros = 0
ones = 0
for i in range(0, len(binaryA)):
    if binaryA[i] == 0:
        zeros = zeros + 1
    elif binaryA[i] == 1:
        ones = ones + 1
print("These many zeros: ", zeros, "\nThese many ones: ", ones)
