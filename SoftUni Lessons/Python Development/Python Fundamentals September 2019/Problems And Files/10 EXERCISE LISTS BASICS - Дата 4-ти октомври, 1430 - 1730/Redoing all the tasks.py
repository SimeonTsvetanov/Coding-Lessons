def invert_values():
    print([abs(int(num)) if int(num) < 0 else -abs(int(num)) for num in input().split(" ")])


def multiples_list():
    factor, count = int(input()), int(input())
    nums = [num for num in range(factor, (factor * count) + 1, factor)]
    print(nums)


def football_cards():
    team_a_players = 11
    team_b_players = 11

    red_cards = list(set(input().split(" ")))
    game_was_terminated = False

    for red_card in red_cards:
        if "A" in red_card:
            team_a_players -= 1
        else:
            team_b_players -= 1
        if team_a_players < 7 or team_b_players < 7:
            game_was_terminated = True
            break

    print(f"Team A - {team_a_players}; Team B - {team_b_players}")
    if game_was_terminated:
        print(f"Game was terminated")


def number_beggars():
    offers = [int(num) for num in input().split(", ")]
    beggars_count = int(input())
    beggars = [0 for num in range(beggars_count)]

    current_beggar = 0

    while True:
        if len(offers) == 0:
            break
        beggars[current_beggar] += offers.pop(0)
        if current_beggar == beggars_count - 1:
            current_beggar = 0
            continue
        current_beggar += 1
    print(beggars)


def faro_shuffle():
    cards = [card for card in input().split(" ")]
    times_to_split = int(input())

    for each_time in range(times_to_split):
        shuffled_list = []
        for (a, b) in zip(cards[:len(cards) // 2], cards[len(cards) // 2:]):
            shuffled_list.append(a)
            shuffled_list.append(b)
        cards = shuffled_list

    print(cards)


def survival_of_the_biggest():
    nums = list(map(int, input().split(" ")))
    [nums.remove(min(nums)) for each_time in range(int(input()))]
    print(", ".join(str(num) for num in nums))


def easter_gifts():
    gifts = input().split(" ")

    while True:
        command = input().split(" ")
        if command[0] == "No":
            break
        elif command[0] == "OutOfStock":
            gifts = ["None" if gift == command[1] else gift for gift in gifts]
        elif command[0] == "Required":
            # gifts[int(command[2])] = command[1] if (0 <= int(command[2]) < len(gifts)) else "pass"
            if 0 <= int(command[2]) <= len(gifts) - 1:
                gifts.pop(int(command[2]))
                gifts.insert(int(command[2]), command[1])
        elif command[0] == "JustInCase":
            gifts[-1] = command[1]

    print(" ".join([gift for gift in gifts if gift != "None"]))


if __name__ == '__main__':
    # invert_values()
    # multiples_list()
    # football_cards()
    # number_beggars()
    # faro_shuffle()
    # survival_of_the_biggest()
    # easter_gifts()
    # The rest of the tasks are to long to spend time soling them again ...