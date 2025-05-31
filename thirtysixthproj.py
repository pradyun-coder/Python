elements = [2, 81]
def counter(elements, a, i):
    if i == len(elements):
        print(a)
        return
    a = a + 1
    counter(elements, a, i +1)

counter(elements, 0, 0)