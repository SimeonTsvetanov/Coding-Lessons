def get_magic_triangle(n):
    a = []
    count = 0
    for i in range(n):
        a.append([])
        a[i].append(1)
        count += 1
        if count == 1:
            continue
        for j in range(1, i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if n != 0:
            a[i].append(1)
    return a


get_magic_triangle(5)
