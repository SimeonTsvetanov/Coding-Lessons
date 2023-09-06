result = "Welcome to Hogwarts."

while True:
    name = input()
    if name == "Voldemort":
        result = "You must not speak of that name!"
        break
    if name == "Welcome!":
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

print(result)
