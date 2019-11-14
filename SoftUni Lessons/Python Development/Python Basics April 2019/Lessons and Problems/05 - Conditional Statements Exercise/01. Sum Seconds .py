time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

# това е единият начин за принтиране на секунди чрез форматиране за добавяне на 0та :)
# print(f"{minutes}:{seconds:02d}")

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
