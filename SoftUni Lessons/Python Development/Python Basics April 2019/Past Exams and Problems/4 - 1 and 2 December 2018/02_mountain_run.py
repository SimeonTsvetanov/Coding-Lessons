import math

record_in_seconds = float(input())
distance_meters = float(input())
time_seconds_for_one_meter = float(input())

georgi_time_clean = distance_meters * time_seconds_for_one_meter
georgi_time_minus_50_seconds = math.floor(distance_meters / 50) * 30
georgi_time = georgi_time_clean + georgi_time_minus_50_seconds

if georgi_time < record_in_seconds:
    print(f"Yes! The new record is {georgi_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record_in_seconds - georgi_time):.2f} seconds slower.")
