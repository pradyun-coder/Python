data = [100, 50, 75, 150]
differences = []
count = 0
def investment(prices, diff, i):
    if i == len(prices):
        return max(diff), min(diff)
    b = i
    while b< len(prices):
        diff.append(prices[b]-prices[i])
        b = b +1
    return investment(prices, diff, i +1)
print(investment(data, differences, count))
