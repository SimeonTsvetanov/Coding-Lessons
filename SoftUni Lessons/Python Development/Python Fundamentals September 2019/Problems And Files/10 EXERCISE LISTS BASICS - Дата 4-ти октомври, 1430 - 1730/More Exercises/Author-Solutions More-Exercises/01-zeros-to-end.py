elements = input().split(", ")
zeros_count = len(list(filter(lambda x: x == "0", elements)))
filtered_elements = list(map(lambda y: int(y), list(filter(lambda x: x != "0", elements))))
for x in range(zeros_count):
    filtered_elements.append(0)
print(filtered_elements) 