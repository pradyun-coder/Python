#gcd finder
number6 = input("Enter a number")
number5 = input("Enter another number")
factors = []
nofactors = 0
if number6<=number5:
    maxcount = int(number6)
else:
    maxcount = int(number5)
for i in range (1, maxcount):
    if int(number6)%int(i) == 0 and int(number5)%int(i) == 0:
        factors.append(i)
        nofactors = nofactors +1
print(factors[nofactors-1])
