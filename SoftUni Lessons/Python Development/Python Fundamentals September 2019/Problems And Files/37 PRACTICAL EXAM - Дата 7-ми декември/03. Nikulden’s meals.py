guests = {}
un_liked_meals = 0

while True:
    command = input().split("-")
    if command[0] == "Stop":
        break
    elif command[0] == "Like":
        like_guest = command[1]
        like_meal = command[2]
        if like_guest not in guests:
            guests[like_guest] = [like_meal]
        elif like_guest in guests:
            if like_meal not in guests[like_guest]:
                guests[like_guest] += [like_meal]

    elif command[0] == "Unlike":
        unlike_guest = command[1]
        unlike_meal = command[2]

        if unlike_guest in guests:
            if unlike_meal in guests[unlike_guest]:
                print(f"{unlike_guest} doesn't like the {unlike_meal}.")
                un_liked_meals += 1
                guests[unlike_guest].remove(unlike_meal)
            else:
                print(f"{unlike_guest} doesn't have the {unlike_meal} in his/her collection.")
        else:
            print(f"{unlike_guest} is not at the party.")


for guest, meals in sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {un_liked_meals}")
