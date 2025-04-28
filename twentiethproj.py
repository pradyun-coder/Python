
bitscheck = input("BIT?")
bits = []

numA = input("Enter number")
for i in range(numA):
    bits.append(i)
bitsval = 0

for i in range(0, len(bits)):
    for j in range(i +1, len(bits)):
        if bits[j] == int(bitscheck):
            bitsval = bitsval +1
if bitsval >= 0:
    print("Yes this repeats")
