times = int(input())

from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid = 0

total = 0

for i in range(times):
    current_number = int(input())
    if 0 <= current_number <= 9:
        total += current_number * 0.2
        from_0_9 += 1
    elif 10 <= current_number <= 19:
        total += current_number * 0.3
        from_10_19 += 1
    elif 20 <= current_number <= 29:
        total += current_number * 0.4
        from_20_29 += 1
    elif 30 <= current_number <= 39:
        total += 50
        from_30_39 += 1
    elif 40 <= current_number <= 50:
        total += 100
        from_40_50 += 1
    else:
        total = total / 2
        invalid += 1

print(f"{total:.2f}")
print(f"From 0 to 9: {(from_0_9 / times * 100):.2f}%")
print(f"From 10 to 19: {(from_10_19 / times * 100):.2f}%")
print(f"From 20 to 29: {(from_20_29 / times * 100):.2f}%")
print(f"From 30 to 39: {(from_30_39 / times * 100):.2f}%")
print(f"From 40 to 50: {(from_40_50 / times * 100):.2f}%")
print(f"Invalid numbers: {(invalid / times * 100):.2f}%")
