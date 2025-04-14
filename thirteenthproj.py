#gcd finder
number6 = input("Enter a number")
number5 = input("Enter another number")

if number6<=number5:
    maxcount = int(number6)
    mincount = int(number5)
else:
    maxcount = int(number5)
    mincount = int(number6)
    
while maxcount%mincount != 0:
    maxcount = maxcount + 1
    if maxcoun%mincount = 0:
        break

print(maxcount)
