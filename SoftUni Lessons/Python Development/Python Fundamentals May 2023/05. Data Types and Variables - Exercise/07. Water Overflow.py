n = int(input())
tank = 0

for i in range(n):
    liters = int(input())
    if tank + liters <= 255:
        tank += liters
    else:
        print(f"Insufficient capacity!")

print(tank)
