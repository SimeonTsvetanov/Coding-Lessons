names = []

while True:
    name = input()
    if name == "End":
        print(f"{len(names)} people remaining.")
        break
    elif name == "Paid":
        [print(n) for n in names]
        names = []
    else:
        names.append(name)
