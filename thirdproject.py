import random
import tkinter

Capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Special = ['!', '@', '#', '$', '%', '&', '*', '₹']
length = 13
Sreps = random.randint(1, length)
Creps = length - Sreps - random.randint(1, length)
Nreps = length - Sreps - Creps - random.randint(1, length)
Spreps = length - Sreps - Creps - Nreps

partA = random.choices(Capitals, k = Creps)
partB = random.choices(Numbers, k = Nreps)
partC = random.choices(Small, k = Sreps)
partD = random.choices(Special, k = Spreps)
pwd = [*partA, *partB, *partC, *partD]
random.shuffle(pwd)
Password = "".join(map(str, pwd))
print(Password)

