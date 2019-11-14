man = int(input())
woman = int(input())
tables = int(input())
counter_tables = 0

for date_man in range(1, man + 1):
    for date_woman in range(1, woman + 1):
        counter_tables += 1
        if counter_tables > tables:
            break
        print(f"({date_man} <-> {date_woman})", end=" ")
