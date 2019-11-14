"""
Programming Fundamentals Mid Exam - 2 November 2019 Group 1
Check your code: https://judge.softuni.bg/Contests/1859/Programming-Fundamentals-Mid-Exam-2-November-2019-Group-1

SUPyF2 P.-Mid-Exam/2 November 2019/1. - Wizard Poker

Problem:
The world is threatened by an enemy never seen before. Your hero's weapon seems to be useless against the enemy.
But your hero has a super strong arsenal full of powerful magic cards and will challenge the enemy to a card duel
to the death and he needs your help to create a deck.
Create a program that adds, inserts, removes and swaps cards in a new deck.
On the first line, you will receive all cards in the form of strings separated by ":".

Until you receive the "Ready" command, you will get commands in the format:
•	Add {card name}
•	Adds the card to the end of the deck.
•	If the card doesn't exist in print "Card not found."
•	Insert {card name} {index}
•	Insert the card at the given index of the deck.
•	If the card doesn't exist or the index is invalid print "Error!"
•	Remove {card name}
•	Remove the card from the deck.
•	If the card doesn't exist in print "Card not found."
•	Swap {card name 1} {card name 2}
•	Swap the positions of the cards.
•	Input will always be valid
•	Shuffle deck
•	Reverse the deck
When you receive the "Ready" command print the cards in the deck separated by space.

Input:
•	On the 1st line, you will receive the arsenal of all cards available separated by ":".
•	On the next lines, until you receive the "Ready" command you will receive commands to arrange your deck.

Output:
•	Print the cards in your deck on a single line, separated by a single space.

Examples:

Input:                                          Output:
Innervate:Moonfire:Pounce:Claw:Wrath:Bite       Wrath Pounce Claw Moonfire
Add Moonfire
Add Pounce
Add Bite
Add Wrath
Insert Claw 0
Swap Claw Moonfire
Remove Bite
Shuffle deck
Ready

Comments:
First command is Add Moofire and now our deck has one card in it.
1. Moonfire Pounce
2. Moonfire Pounce Bite
3. Moonfire Pounce Bite Wrath
4. Claw Moonfire Pounce Bite Wrath
5. Moonfire Claw Pounce Bite Wrath
6. Moonfire Claw Pounce Wrath
7. Wrath Pounce Claw Moonfire

Input:
Wrath:Pounce:Lifeweaver:Exodia:Aso:Pop
Add Pop
Add Exodia
Add Aso
Remove Wrath
Add SineokBqlDrakon
Shuffle deck
Insert Pesho 0
Ready

Output:
Card not found.
Card not found.
Error!
Aso Exodia Pop
"""
cards = input().split(":")
new_cards = []

while True:
    command = input().split()
    if command[0] == "Ready":
        print(*new_cards)
        break

    elif command[0] == "Add":
        add_card_name = command[1]
        if add_card_name in cards:
            new_cards.append(add_card_name)
        else:
            print(f"Card not found.")

    elif command[0] == "Insert":
        insert_card_name = command[1]
        insert_index = int(command[2])
        if insert_card_name in cards and 0 <= insert_index < len(new_cards):
            new_cards.insert(insert_index, insert_card_name)
        else:
            print("Error!")

    elif command[0] == "Remove":
        remove_card_name = command[1]
        if remove_card_name in new_cards:
            new_cards.remove(remove_card_name)
        else:
            print(f"Card not found.")

    elif command[0] == "Swap":
        swap_card_1 = command[1]
        swap_card_2 = command[2]
        index_swap_card_1 = new_cards.index(swap_card_1)
        index_swap_card_2 = new_cards.index(swap_card_2)
        new_cards.remove(swap_card_1)
        new_cards.remove(swap_card_2)
        new_cards.insert(index_swap_card_1, swap_card_2)
        new_cards.insert(index_swap_card_2, swap_card_1)

    elif command[0] == "Shuffle":
        new_cards = reversed(new_cards)

