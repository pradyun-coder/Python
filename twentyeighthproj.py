import math
numA = input("Enter number")
numB = input("enter the base of the power")

binaryA = []

for i in range (round(math.log(int(numA), int(numB))), -1, -1):
    if int(numB)**i <= int(numA):
        binaryA.append(1)
        numA = int(numA) - int(numB)**i
    else:
        binaryA.append(0)

counter = 0
for i in binaryA:
    if i == 1:
        counter += 1

if counter == 1:
    print("Yes it can be represented through base^x")
else:
    print("Sorry, it is not")