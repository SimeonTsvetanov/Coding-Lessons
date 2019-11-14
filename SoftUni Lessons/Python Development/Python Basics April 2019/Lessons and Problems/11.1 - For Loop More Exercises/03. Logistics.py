cargo = int(input())

total = 0
times_with_bus = 0
times_with_truck = 0
times_with_train = 0

for i in range(1, cargo + 1):
    size = int(input())
    total += size
    if size <= 3:
        times_with_bus += size
    elif 4 <= size <= 11:
        times_with_truck += size
    elif size >= 12:
        times_with_train += size

average_per_ton = ((times_with_bus * 200) + (times_with_truck * 175) + (times_with_train * 120)) / total

print(f"{average_per_ton:.2f}")
print(f"{(times_with_bus / total * 100):.2f}%")
print(f"{(times_with_truck / total * 100):.2f}%")
print(f"{(times_with_train / total * 100):.2f}%")

