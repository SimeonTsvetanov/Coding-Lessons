aim = int(input())
start = aim - 30
bad_count = 0
total_jumps = 0

while not(start > aim):
    if bad_count == 3:
        break
    jump = int(input())
    total_jumps += 1
    if jump > start:
        start += 5
        bad_count = 0
    else:
        bad_count += 1

if bad_count == 3:
    print(f"Tihomir failed at {start}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {start - 5}cm after {total_jumps} jumps.")
