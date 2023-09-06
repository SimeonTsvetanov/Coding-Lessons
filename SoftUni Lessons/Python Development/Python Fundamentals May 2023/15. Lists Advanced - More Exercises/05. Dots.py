# Task solved by Chat GPT:

# To solve this task, we can use Depth-First Search (DFS)
# to find the largest count of connected dots.
# Let's write a Python function to accomplish this:

# The dfs function is a recursive depth-first search that
# counts the number of connected dots starting from a given position (i, j).

# The largest_count_of_dots function iterates through the board and
# finds the largest count of connected dots using DFS.
# Make sure to convert the input strings into lists of strings representing
# the rows of the board before passing them to the function.
# The function will then return the maximum count of dots that could be connected at once,
# as shown in the output.

def dfs(board, i, j, visited):
    rows, cols = len(board), len(board[0])
    if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != '.' or visited[i][j]:
        return 0

    visited[i][j] = True
    count = 1

    count += dfs(board, i - 1, j, visited)  # Up
    count += dfs(board, i + 1, j, visited)  # Down
    count += dfs(board, i, j - 1, visited)  # Left
    count += dfs(board, i, j + 1, visited)  # Right

    return count


def largest_count_of_dots(n, board):
    rows, cols = n, len(board[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_count = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.' and not visited[i][j]:
                count = dfs(board, i, j, visited)
                max_count = max(max_count, count)

    return max_count


n = int(input())
board = [input() for _ in range(n)]

max_count = largest_count_of_dots(n, [row.split() for row in board])
print(max_count)
