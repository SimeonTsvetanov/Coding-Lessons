# x = lambda a: abs(a)
# print([x(float(num)) for num in input().split()])
numbers = map(float, input().split(" "))
result = map(abs, numbers)
print(list(result))

