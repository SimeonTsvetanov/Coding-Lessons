entry = float(input())

while entry >= 0:
    if entry < 0:
        break
    print(f"Result: {(entry * 2):.2f}")
    entry = float(input())

print("Negative number!")
