n = int(input())

best = {
    'value': 0,
    'weight': 0,
    'time': 0,
    'quality': 0
}

for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value >= best['value']:
        best['value'] = int(value)
        best['weight'] = weight
        best['time'] = time
        best['quality'] = quality

print(f'{best["weight"]} : {best["time"]} = {best["value"]} ({best["quality"]})')
