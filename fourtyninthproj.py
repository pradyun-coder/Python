arrB = [1, 2, 3, 4, 5]

def array_reverse(arrb):
    a = []
    i = len(arrb) -1
    while i > -1:
        a.append(arrb[i])
        i = i - 1
    print(a)
array_reverse(arrB)