import random
numbers = []
text = input("Enter a string")
for i in (text):
    numbers.append(i)
d = len(numbers)
a = []
b = []
c = 0
while c <= 2*c + 1:
    b = random.sample(numbers, k = random.randint(0, d))
    if b not in a:
        print(b)
        a.append(b)
        c = c + 1

