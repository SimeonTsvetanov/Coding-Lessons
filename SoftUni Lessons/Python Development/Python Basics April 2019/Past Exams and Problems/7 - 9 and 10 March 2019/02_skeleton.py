minutes_control = int(input())
seconds_control = int(input())
length_slope = float(input())
seconds_for_100_meters = int(input())

total_control_in_seconds = minutes_control * 60 + seconds_control
time_slow = (length_slope / 120) * 2.5
marin_time = (length_slope / 100) * seconds_for_100_meters - time_slow

if marin_time <= total_control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {(marin_time - total_control_in_seconds):.3f} second slower.")
