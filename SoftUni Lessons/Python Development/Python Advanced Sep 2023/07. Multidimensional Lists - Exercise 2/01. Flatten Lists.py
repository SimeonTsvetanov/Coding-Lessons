matrix = [[el for el in r.split()] for r in input().split("|")][::-1]
print(' '.join([j for sub in matrix for j in sub]))
