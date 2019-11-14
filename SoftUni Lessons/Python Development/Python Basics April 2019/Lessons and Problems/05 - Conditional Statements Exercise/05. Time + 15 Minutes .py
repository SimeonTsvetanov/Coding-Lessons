hour = int(input())
minute = int(input())

minute = minute + 15
total = (hour * 60) + minute

hour = total // 60
minute = total % 60

if hour > 23:
    hour = hour - 24

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")

# print(f"{hour}:{minute:02d}")

