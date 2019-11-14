import math

record = float(input())
distance_meters = float(input())
time_seconds = float(input())

real_time = distance_meters * time_seconds
added_time = math.floor(distance_meters / 15) * 12.5
total_time = real_time + added_time

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record - total_time):.2f} seconds slower.")
