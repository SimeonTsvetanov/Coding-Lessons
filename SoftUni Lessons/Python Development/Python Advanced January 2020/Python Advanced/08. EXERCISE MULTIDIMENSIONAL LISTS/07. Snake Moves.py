rows, cols = list(map(int, input().split()))
matrix = [['' for col in range(cols)] for row in range(rows)]
snake = [symbol for symbol in input()]
snake_index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            if snake_index == len(snake):
                snake_index = 0
            matrix[row][col] = snake[snake_index]
            snake_index += 1
    elif row % 2 != 0:
        for col in range(cols - 1, -1, -1):
            if snake_index == len(snake):
                snake_index = 0
            matrix[row][col] = snake[snake_index]
            snake_index += 1

[print(''.join(row)) for row in matrix]
