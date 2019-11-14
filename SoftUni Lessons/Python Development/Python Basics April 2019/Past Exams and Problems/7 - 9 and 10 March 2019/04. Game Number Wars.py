name_player_one = input()
name_player_two = input()

player_one_points = 0
player_two_points = 0

command = None

while command != "End of game":
    command = input()
    if command == "End of game":
        break
    player_one_card = int(command)
    player_two_card = int(input())
    if player_one_card > player_two_card:
        player_one_points += abs(player_one_card - player_two_card)
    elif player_two_card > player_one_card:
        player_two_points += abs(player_two_card - player_one_card)
    elif player_one_card == player_two_card:
        final_one_card = int(input())
        final_two_card = int(input())
        if final_one_card > final_two_card:
            player_two_points = 0
        elif final_two_card > final_one_card:
            player_one_points = 0
        print("Number wars!")
        break

if command == "End of game":
    print(f"{name_player_one} has {player_one_points} points")
    print(f"{name_player_two} has {player_two_points} points")
else:
    if player_one_points > player_two_points:
        print(f"{name_player_one} is winner with {player_one_points} points")
    else:
        print(f"{name_player_two} is winner with {player_two_points} points")