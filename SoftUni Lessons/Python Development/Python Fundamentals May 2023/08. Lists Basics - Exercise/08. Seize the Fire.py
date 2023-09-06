def valid(type_of_fire, value_of_fire):
    return (type_of_fire == "High" and (81 <= value_of_fire <= 125)) or \
            (type_of_fire == "Medium" and (51 <= value_of_fire <= 80)) or \
            (type_of_fire == "Low" and (1 <= value_of_fire <= 50))


done_cells = []
effort = 0
total_fire = 0

cells = [c for c in input().split('#')]
water = int(input())

for cell in cells:
    type_fire = cell.split(' = ')[0]
    value_fire = int(cell.split(' = ')[1])

    if valid(type_fire, value_fire) and water - value_fire >= 0:
        water -= value_fire
        done_cells.append(value_fire)
        total_fire += value_fire
        effort += 0.25 * value_fire

result = f"Cells:\n"
for cell in done_cells:
    result += f"- {cell}\n"
result += f"Effort: {effort:.2f}\nTotal Fire: {total_fire}"

print(result)
