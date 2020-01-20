n = int(input())

start_pump = 0
fuel_left = 0

for i in range(n):
    gas_pump, distance_to_next = [int(x) for x in input().split()]
    fuel_left += gas_pump
    if fuel_left >= distance_to_next:
        fuel_left -= distance_to_next
    else:
        start_pump = i + 1
        fuel_left = 0

print(start_pump)
