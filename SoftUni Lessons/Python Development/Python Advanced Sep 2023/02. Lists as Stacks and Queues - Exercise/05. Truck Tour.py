"""
There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). For each
petrol pump, you will receive two pieces of information (separated by a single space):

- The amount of petrol the petrol pump will give you
- The distance from that petrol pump to the next petrol pump (kilometers)

You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol
per 1 kilometer, and its tank has infinite petrol capacity.

In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given
amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. You never
miss filling its tank at a petrol pump.
"""

# On the first line, you will receive the number of petrol pumps - N
n = int(input())

# On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance
# between that petrol pump and the next petrol pump, separated by a single space

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
