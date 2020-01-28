def solve():
    matrix = [[int(num) for num in input().split(", ")] for line in range(int(input()))]
    primary_diagonal = [matrix[x][x] for x in range(len(matrix))]
    secondary_diagonal = [matrix[x][len(matrix) - x - 1] for x in range(len(matrix))]
    print(f"First diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
    print(f"Second diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")


if __name__ == '__main__':
    solve()
