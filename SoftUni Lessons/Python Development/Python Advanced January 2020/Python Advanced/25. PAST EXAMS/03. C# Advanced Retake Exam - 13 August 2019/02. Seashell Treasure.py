beach = []
collected_seashells = []
seagull_shells_count = 0

for _ in range(int(input())):
    beach.append([shell for shell in input().split()])

while True:
    command = input().split()
    if command[0] == "Sunset":
        break

    elif command[0] == "Collect":
        collect_row = int(command[1])
        collect_col = int(command[2])
        if (0 <= collect_row < len(beach)) and (0 <= collect_col < len(beach[collect_row])):
            if beach[collect_row][collect_col] != "-":
                collected_seashells.append(beach[collect_row][collect_col])
                beach[collect_row][collect_col] = "-"

    elif command[0] == "Steal":
        row = int(command[1])
        col = int(command[2])
        direction = command[3]
        if (0 <= row < len(beach)) and 0 <= col < len(beach[row]):
            # The cell exists
            if beach[row][col] != "-":
                seagull_shells_count += 1
                beach[row][col] = "-"

                for step in range(3):

                    if direction == "up":
                        if (0 <= (row - 1) < len(beach)) and 0 <= col < len(beach[row - 1]):
                            # The row cell exists:
                            row -= 1
                            if beach[row][col] != "-":
                                seagull_shells_count += 1
                                beach[row][col] = "-"
                        else:
                            break

                    elif direction == "down":
                        if (0 <= (row + 1) < len(beach)) and 0 <= col < len(beach[row + 1]):
                            # The row cell exists:
                            row += 1
                            if beach[row][col] != "-":
                                seagull_shells_count += 1
                                beach[row][col] = "-"
                        else:
                            break

                    elif direction == "left":
                        if (0 <= row < len(beach)) and 0 <= (col - 1) < len(beach[row]):
                            # The col cell exists:
                            col -= 1
                            if beach[row][col] != "-":
                                seagull_shells_count += 1
                                beach[row][col] = "-"
                        else:
                            break

                    elif direction == "right":
                        if (0 <= row < len(beach)) and 0 <= (col + 1) < len(beach[row]):
                            # The col cell exists:
                            col += 1
                            if beach[row][col] != "-":
                                seagull_shells_count += 1
                                beach[row][col] = "-"
                        else:
                            break

for row in beach:
    print(f" ".join(row))

if len(collected_seashells) > 0:
    print(f"Collected seashells: {len(collected_seashells)} -> {', '.join(collected_seashells)}")
else:
    print(f"Collected seashells: 0")

print(f"Stolen seashells: {seagull_shells_count}")
