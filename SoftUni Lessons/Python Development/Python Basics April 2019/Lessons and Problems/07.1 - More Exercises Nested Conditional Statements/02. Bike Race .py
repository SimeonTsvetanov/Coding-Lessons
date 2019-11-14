juniors_count = int(input())
seniors_count = int(input())
trace_type = input()

juniors_total = 0
seniors_total = 0

if trace_type == "trail":
    juniors_total = 5.50 * juniors_count
    seniors_total = 7 * seniors_count
elif trace_type == "cross-country":
    juniors_total = 8 * juniors_count
    seniors_total = 9.50 * seniors_count
elif trace_type == "downhill":
    juniors_total = 12.25 * juniors_count
    seniors_total = 13.75 * seniors_count
elif trace_type == "road":
    juniors_total = 20 * juniors_count
    seniors_total = 21.50 * seniors_count

total = juniors_total + seniors_total

if trace_type == "cross-country" and (juniors_count + seniors_count) >= 50:
    total -= total * 0.25

total -= total * 0.05

print(f"{total:.2f}")
