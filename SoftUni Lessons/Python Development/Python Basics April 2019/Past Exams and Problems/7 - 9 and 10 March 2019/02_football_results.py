wins = 0
draws = 0
loses = 0

for i in range(0, 3):
    result = input()
    goals = result.split(":")
    a = goals[0]
    b = goals[1]
    if a > b:
        wins += 1
    if a == b:
        draws += 1
    if a < b:
        loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")

