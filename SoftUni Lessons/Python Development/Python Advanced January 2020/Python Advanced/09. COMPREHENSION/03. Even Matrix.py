def even_matrix():
    lines = int(input())
    even = [[int(num) for num in input().split(", ") if int(num) % 2 == 0] for line in range(lines)]
    print(even)


if __name__ == '__main__':
    even_matrix()
