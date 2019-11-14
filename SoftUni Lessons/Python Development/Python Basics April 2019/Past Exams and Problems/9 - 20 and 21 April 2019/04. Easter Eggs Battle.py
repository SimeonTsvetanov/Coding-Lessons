num_eggs_first = int(input())
num_eggs_second = int(input())
command = input()
while command != "End of battle":

    if command == "one":
        num_eggs_second -= 1
    elif command == "two":
        num_eggs_first -= 1

    if num_eggs_first == 0:
        print(f"Player one is out of eggs. Player two has {num_eggs_second} eggs left.")
        break
    elif num_eggs_second == 0:
        print(f"Player two is out of eggs. Player one has {num_eggs_first} eggs left.")
        break
    command = input()
if command == "End of battle":
    print(f"Player one has {num_eggs_first} eggs left.")
    print(f"Player two has {num_eggs_second} eggs left.")