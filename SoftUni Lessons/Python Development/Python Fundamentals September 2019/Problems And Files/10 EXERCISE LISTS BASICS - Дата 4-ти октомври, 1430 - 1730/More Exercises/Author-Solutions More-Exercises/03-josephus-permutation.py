soldiers = input().split(" ")
k = int(input())

result = []
index = k - 1

while True:
    if index >= len(soldiers):
        index = index % len(soldiers)
    result.append(soldiers[index])
    del soldiers[index]
    if len(soldiers) == 0:
        output = "["
        for x in range(len(result) - 1): output += f"{result[x]},"
        output += result[-1] + "]"
        print(output)
        break
    index += k - 1
    if index >= len(soldiers):
        index = index % len(soldiers)