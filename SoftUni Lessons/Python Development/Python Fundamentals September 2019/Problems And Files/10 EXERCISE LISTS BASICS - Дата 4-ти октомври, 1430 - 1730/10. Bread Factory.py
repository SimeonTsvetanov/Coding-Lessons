"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#9

SUPyF2 Lists Basics Exercise - 10. Bread Factory (not included in final score)

Problem:
As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100. You will be given a string,
representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2|event3…"
Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
•	If the event is "rest": you gain energy, the number in the second part.
But your energy cannot exceed your initial energy (100). Print: "You gained {0} energy.".
After that, print your current energy: "Current energy: {0}.".
•	If the event is "order": You've earned some coins, the number in the second part.
Each time you get an order, your energy decreases with 30 points.
o	If you have energy to complete the order, print: "You earned {0} coins.".
o	If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".
•	In any other case you are having an ingredient, you have to buy.
The second part of the event, contains the coins you have to spent and remove from your coins.
o	If you are not bankrupt (coins <= 0) you've bought the ingredient successfully,
and you should print ("You bought {ingredient}.")
o	If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
If you managed to handle all events through the day, print on the next three lines:
"Day completed!", "Coins: {coins}", "Energy: {energy}".
Input / Constraints
You receive a string, representing the working day events, separated with '|' (vertical bar): " event1|event2|event3…".
Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")
Output
Print the corresponding messages, described above.

Examples:
Input:
rest-2|order-10|eggs-100|rest-10

Output:
You gained 0 energy.
Current energy: 100.
You earned 10 coins.
You bought eggs.
You gained 10 energy.
Current energy: 80.
Day completed!
Coins: 10
Energy: 80

Input:
order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000

Output:
You earned 10 coins.
You earned 10 coins.
You earned 10 coins.
You bought flour.
You had to rest!
Closed! Cannot afford oven.
"""
energy = 100
coins = 100
events = input().split("|")

day_finished = True

for event in events:
    info = event.split("-")
    event_or_ingredient = info[0]
    number = int(info[1])

    if event_or_ingredient == "rest":
        if (number + energy) > 100:
            more_energy = (energy + number) - 100
            number -= more_energy
        energy += number
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            day_finished = False
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break

if day_finished:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
