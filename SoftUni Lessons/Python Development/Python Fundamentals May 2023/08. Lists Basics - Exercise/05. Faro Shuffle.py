cards = [card for card in input().split(" ")]
times_to_split = int(input())

for each_time in range(times_to_split):
    shuffled_list = []
    for (a, b) in zip(cards[:len(cards)//2], cards[len(cards)//2:]):
        shuffled_list.append(a)
        shuffled_list.append(b)
    cards = shuffled_list

print(cards)
