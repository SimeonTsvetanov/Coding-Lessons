energy = 100
coins = 100
events = [e for e in input().split('|')]
closed = False

for data in events:
    event_ingredient = data.split('-')[0]
    value = int(data.split('-')[1])

    if event_ingredient == 'rest':
        if value + energy > 100:
            extra_energy = (energy + value) - 100
            value -= extra_energy
        energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif event_ingredient == 'order':
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy = min(100, energy + 50)
            print(f'You had to rest!')
    else:
        if coins - value >= 0:
            print(f"You bought {event_ingredient}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            closed = True
            break

if not closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
