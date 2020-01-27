def flattening_matrix():
    lines = int(input())
    matrix = [[int(num) for num in input().split(", ")] for line in range(lines)]
    flattened = [num for row in matrix for num in row]
    print(flattened)


if __name__ == '__main__':
    flattening_matrix()
