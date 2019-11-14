clients_man = int(input()) + 1
clients_woman = int(input()) + 1
max_count_tables = int(input())

max_count_spaces = max_count_tables * 2

for man in range(1, clients_man):
    for woman in range(1, clients_woman):
        if max_count_spaces == 0:
            break
        print(f"({man} <-> {woman})", end=" ")
        max_count_spaces -= 2
