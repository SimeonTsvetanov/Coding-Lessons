count_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for egg in range(count_eggs):
    color = input()
    if color == "red":
        red += 1
    if color == "orange":
        orange += 1
    if color == "blue":
        blue += 1
    if color == "green":
        green += 1

colors = {'red': red, 'orange': orange, 'blue': blue, 'green': green}
max_colors_name = max(colors, key=colors.get)

colors_count = {red, orange, blue, green}
max_colors_count = max(colors_count)

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_colors_count} -> {max_colors_name}")




