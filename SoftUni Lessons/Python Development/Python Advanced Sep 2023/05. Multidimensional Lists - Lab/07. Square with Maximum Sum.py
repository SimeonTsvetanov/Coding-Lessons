row, col = [int(x) for x in input().split(', ')]
m = [[int(x) for x in input().split(', ')] for r in range(row)]

square = []
max_sum = 0

for r in range(len(m) - 1):
    for c in range(len(m[r]) - 1):
        current_square = [m[r][c], m[r][c + 1], m[r + 1][c], m[r + 1][c + 1]]
        current_sum = sum(current_square)
        if current_sum > max_sum:
            square = current_square
            max_sum = current_sum

print(f"{square[0]} {square[1]}\n{square[2]} {square[3]}")
print(max_sum)
