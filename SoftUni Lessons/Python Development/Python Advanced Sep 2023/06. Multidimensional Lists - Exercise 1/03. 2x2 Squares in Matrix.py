row, col = [int(x) for x in input().split(' ')]
m = [[str(x) for x in input().split(' ')] for r in range(row)]

count_same_squares = 0

for r in range(len(m) - 1):
    for c in range(len(m[r]) - 1):
        current_square = [m[r][c], m[r][c + 1], m[r + 1][c], m[r + 1][c + 1]]
        if len(set(current_square)) == 1:
            count_same_squares += 1

print(count_same_squares)
