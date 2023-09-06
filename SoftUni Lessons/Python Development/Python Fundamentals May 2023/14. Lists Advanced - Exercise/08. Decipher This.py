message = [word for word in input().split(' ')]

decoded = []

for word in message:
    code = ''.join([c for c in word if c.isdigit()])
    rest = list(''.join([c for c in word if c.isalpha()]))
    rest[0], rest[-1] = rest[-1], rest[0]
    decoded.append(chr(int(code)) + ''.join(rest))


print(*decoded)
