n = int(input())

free_chairs = 0

for i in range(1, n + 1):
    data = input().split(' ')
    chairs = len([c for c in data[0]])
    visitors = int(data[1])

    if chairs - visitors < 0:
        print(f"{abs(chairs - visitors)} more chairs needed in room {i}")

    free_chairs += chairs - visitors

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
