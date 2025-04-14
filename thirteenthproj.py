#lcm finder
number6 = input("Enter a number")
number5 = input("Enter another number")

if number6<=number5:
    mincount = int(number6)
    maxcount = int(number5)
else:
    mincount = int(number5)
    maxcount = int(number6)
    
while maxcount%mincount != 0:
    if maxcount%mincount == 0:
        break
    maxcount = maxcount + 1

print(maxcount)
