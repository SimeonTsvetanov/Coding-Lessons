total = int(input())

array = []
n = 1

while total > 0:
    el = 2 * (n ** 2)
    if el <= total:
        array.append(el)
        total -= el
    else:
        array.append(total)
        total -= el
    n += 1

print(array)
