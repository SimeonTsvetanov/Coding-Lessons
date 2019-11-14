batch = int(input())

for i in range(1, batch + 1):
    flour = False
    eggs = False
    sugar = False
    while True:
        product = input()
        if product == "flour":
            flour = True
        elif product == "eggs":
            eggs = True
        elif product == "sugar":
            sugar = True
        if product == "Bake!":
            if flour and eggs and sugar:
                print(f"Baking batch number {i}...")
                break
            else:
                print("The batter should contain flour, eggs and sugar!")

