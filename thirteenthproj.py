#factor finder
number2 = input("Enter a number")
factors=[]
for i in range (1, int(number2) + 1):
    if int(number2)%int(i) == 0:
        factors.append(i)
print(factors)
