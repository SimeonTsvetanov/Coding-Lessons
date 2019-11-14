import math
count_games = int(input())
start_points = int(input())

total_points = start_points
wins = 0

for i in range(count_games):
    score = input()
    if score == "W":
        total_points += 2000
        wins += 1
    elif score == "F":
        total_points += 1200
    elif score == "SF":
        total_points += 720

print(f"Final points: {total_points}")
print(f"Average points: {math.floor((total_points - start_points) / count_games)}")
print(f"{(wins / count_games * 100):.2f}%")
