rows, cols = list(map(int, input().split()))
matrix = [["" for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        first_last = chr(row + 97)
        middle = chr(row + col + 97)
        matrix[row][col] = f"{first_last}{middle}{first_last}"

[print(' '.join(row)) for row in matrix]
