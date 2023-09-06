sides = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    tokens = command.split(" | ")

    if len(tokens) == 2:
        side, user = tokens
        is_contained = False
        for key, value in sides.items():
            if user in value:
                is_contained = True
        if not is_contained:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)

    else:
        tokens = command.split(" -> ")
        user, side = tokens

        for key, value in sides.items():
            if user in value:
                sides[key].remove(user)

        if side not in sides:
            sides[side] = []
        sides[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in sides.items():
    if len(users) >= 1:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
