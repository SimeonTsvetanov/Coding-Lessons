print(sorted([name for name in input().split(', ')], key= lambda x: (-len(x), x)))
