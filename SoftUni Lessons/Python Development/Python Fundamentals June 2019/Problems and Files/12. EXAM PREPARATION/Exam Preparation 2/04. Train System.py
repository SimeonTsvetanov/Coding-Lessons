"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1578#3

SUPyF Exam Preparation 2 - 04. Train System
Problem:
The Bulgarian Dreadful Zug Company (BDZ) just upgraded their ticket systems from something running on DOS
5 to a state-of-the-art system running a fancy web app. Of course, nobody bothered to migrate all the discount
cards over to the new system, so all the passengers trying to buy a ticket with a discount nearly miss their train,
since the cashier, grandma Penka, needs to enter it into the new system. Luckily, she heard about this great thing,
called Python from her neighbor, grandma Gina, and how she can use it to automate this task.
In this problem, you assume the role of grandma Penka. You have a 15-minute lunch break, so you decide to use that time
to write up a Python script to migrate all the data.
Input / Constraints
•	On the first line, you will receive the number of existing cards N – integer in range [0-5]
•	On the next N lines, you will receive the existing cards in the format “firstName lastName ticketNum”.
o	Existing cards will always have a valid card number
•	Then, until you receive the command “time to leave!”, keep reading lines in the format:
o	“createTicket firstName lastName destination cardNumber”
The input data will always be in the format specified. There is no need to check it explicitly.
When you receive all the existing cards, insert them into the system.
Cards are tied to the person’s full name (first name + space (“ “) + last name). A person can have multiple cards.
After that, your lunch break is over and you need to start issuing tickets to people again.
A standard “issue ticket” command looks like this:
•	“createTicket firstName lastName destination cardNumber”
You need to check if this person already has a card with that number under that name. If they do,
issue their ticket with the card number. If not, you need to check if the card number is valid.
A valid card number’s digit sum is divisible by 7 (example: 297296  (2+9+7+2+9+6) % 7 == 0  valid).
If the card number is invalid, print “card {cardNumber} is not valid!” and issue the ticket without a discount.
If the card number is valid, but it already belongs to another passenger, print “card {cardNumber} already exists for
another passenger!” and issue the ticket without a discount.
If the card doesn’t already belong to another passenger and is not already in the existing cards,
you need to issue that passenger a card. Insert it into the cards and print (“issuing card {cardNumber}”).
After that, issue them a ticket with a discount.
The price of the ticket is the sum of the ASCII codes of the destination name, divided by 100
•	Example: vidin  v+i+d+i+n  538 / 100  5.38
Every ticket bought with a valid card that belongs to the passenger is 50% cheaper.
Output
When you receive “time to leave!”, print all passengers in the following format:
fullName:
--{destination}: {ticketPrice:.2f}
--{destination}: {ticketPrice:.2f} (using card {cardNumber})
...
total: {ticketPrice:.2f}BGN
Sort the passengers by the sum of their ticket prices (descending).
Sort each passenger’s tickets by the ticket’s price (descending).
If a ticket was bought without a discount, don’t print “using card…” after it.

Examples:
Input:
4
pesho ivanov 297296
ivan tsekov 652530
gosho goshov 547989
ivan tsekov 468845
createTicket pesho ivanov vidin 297296
createTicket ivan petrov ruska_bela 590432
createTicket ivan petrov sofia 590430
createTicket pesho ivanov boychinovtsi 590554
createTicket bay ivan montana 912839
time to leave!

Output:
card 590432 is not valid!
issuing card 590430
issuing card 590554
card 912839 is not valid!
ivan petrov:
--ruska_bela: 10.49lv
--sofia: 2.65lv (using card 590430)
total: 13.14lv
pesho ivanov:
--boychinovtsi: 6.57lv (using card 590554)
--vidin: 2.69lv (using card 297296)
total: 9.26lv
bay ivan:
--montana: 7.50lv
total: 7.50lv

Input:
1
georgi georgiev 586790
createTicket pesho petrov vidin 297296
createTicket pesho petrov montana 630534
createTicket pesho petrov plovdiv 630534
createTicket bay ivan vidin 297296
createTicket bay ivan sofia 111111
createTicket bay ivan montana 111111
createTicket bay ivan mezdra 111111
time to leave!

Output:
issuing card 297296
issuing card 630534
card 297296 already exists for another passenger!
card 111111 is not valid!
card 111111 is not valid!
card 111111 is not valid!
bay ivan:
--montana: 7.50lv
--mezdra: 6.43lv
--vidin: 5.38lv
--sofia: 5.30lv
total: 24.61lv
pesho petrov:
--plovdiv: 3.86lv (using card 630534)
--montana: 3.75lv (using card 630534)
--vidin: 2.69lv (using card 297296)
total: 10.30lv

Input:
3
ivan ivanov 094859
ceko cekov 328994
krali marko 774154
createTicket ivan ivanov montana 094859
createTicket ivan ivanov vidin 094859
createTicket ivan ivanov plovdiv 094859
createTicket krali marko vidin 774154
createTicket krali marko sofia 774154
createTicket bay ivan mezdra 000006
createTicket ceko cekov montana 328994
time to leave!

Output:
card 000006 is not valid!
ivan ivanov:
--plovdiv: 3.86lv (using card 094859)
--montana: 3.75lv (using card 094859)
--vidin: 2.69lv (using card 094859)
total: 10.30lv
bay ivan:
--mezdra: 6.43lv
total: 6.43lv
krali marko:
--vidin: 2.69lv (using card 774154)
--sofia: 2.65lv (using card 774154)
total: 5.34lv
ceko cekov:
--montana: 3.75lv (using card 328994)
total: 3.75lv
"""


class Person:
    def __init__(self, f_name: str, l_name: str, cards: []):
        self.f_name = f_name
        self.l_name = l_name
        self.cards = cards
        self.full_name = f"{f_name} {l_name}:"
        self.tickets = []
        self.total_from_tickets = 0


all_people = []

n = int(input())

for i in range(n):
    first_name, last_name, card_num = input().split()
    # card_num = int(card_num)

    person_in_all_people = False
    for person in all_people:
        if person.f_name == first_name and person.l_name == last_name:
            person_in_all_people = True
            person.cards += [card_num]
    if not person_in_all_people:
        p = Person(f_name=first_name, l_name=last_name, cards=[card_num])
        all_people += [p]

while True:
    command = input()
    if command == "time to leave!":
        break
    create_ticket, first_name_n, last_name_n, destination, card_number = command.split()
    # card_number = int(str_card_number)

    person_already_in_all_people = False
    for person_n in all_people:

        if person_n.f_name == first_name_n and person_n.l_name == last_name_n:
            person_already_in_all_people = True
            person_has_that_card = False
            for card_n in person_n.cards:
                if card_n == card_number:
                    person_has_that_card = True
                    price_discounted_ticket = (sum(list(map(ord, destination))) / 100) / 2
                    discounted_ticket_data = [f"--{destination}: {price_discounted_ticket:.2f}lv (using card {card_number})", price_discounted_ticket]
                    person_n.tickets += [discounted_ticket_data]
                    person_n.total_from_tickets += price_discounted_ticket
                    break

            if not person_has_that_card:
                card_is_valid = ((sum(list(map(int, [int(item) for item in str(card_number)])))) % 7) == 0

                if not card_is_valid:
                    print(f"card {card_number} is not valid!")
                    price_ticket = sum(list(map(ord, destination))) / 100
                    ticket_data = [f"--{destination}: {price_ticket:.2f}lv", price_ticket]
                    person_n.tickets += [ticket_data]
                    person_n.total_from_tickets += price_ticket
                    continue

                someone_else_card = False
                for person_s in all_people:
                    if person_s.f_name != first_name_n and person_s.l_name != last_name_n:
                        for card in person_s.cards:
                            if card_number == card:
                                someone_else_card = True
                                print(f"card {card_number} already exists for another passenger!")
                                price_ticket = sum(list(map(ord, destination))) / 100
                                ticket_data = [f"--{destination}: {price_ticket:.2f}lv", price_ticket]
                                person_n.tickets += [ticket_data]
                                person_n.total_from_tickets += price_ticket

                if card_is_valid and (not someone_else_card):
                    print(f"issuing card {card_number}")
                    person_n.cards += [card_number]
                    price_discounted_ticket = (sum(list(map(ord, destination))) / 100) / 2
                    discounted_ticket_data = [f"--{destination}: {price_discounted_ticket:.2f}lv (using card {card_number})", price_discounted_ticket]
                    person_n.tickets += [discounted_ticket_data]
                    person_n.total_from_tickets += price_discounted_ticket

    if not person_already_in_all_people:
        card_is_valid = ((sum(list(map(int, [int(item) for item in str(card_number)])))) % 7) == 0

        if not card_is_valid:
            print(f"card {card_number} is not valid!")
            price_ticket = sum(list(map(ord, destination))) / 100
            ticket_data = [f"--{destination}: {price_ticket:.2f}lv", price_ticket]
            p = Person(f_name=first_name_n, l_name=last_name_n, cards=["dummy_card"])
            p.tickets += [ticket_data]
            p.total_from_tickets += price_ticket
            all_people += [p]
            continue

        someone_else_card = False
        for person_s in all_people:
            if person_s.f_name != first_name_n or person_s.l_name != last_name_n:
                for card in person_s.cards:
                    if card_number == card:
                        someone_else_card = True
                        print(f"card {card_number} already exists for another passenger!")
                        price_ticket = sum(list(map(ord, destination))) / 100
                        ticket_data = [f"--{destination}: {price_ticket:.2f}lv", price_ticket]
                        p = Person(f_name=first_name_n, l_name=last_name_n, cards=["dummy_card"])
                        p.tickets += [ticket_data]
                        p.total_from_tickets += price_ticket
                        all_people += [p]

        if card_is_valid and (not someone_else_card):
            print(f"issuing card {card_number}")
            p = Person(f_name=first_name_n, l_name=last_name_n, cards=[card_number])
            price_discounted_ticket = (sum(list(map(ord, destination))) / 100) / 2
            discounted_ticket_data = [f"--{destination}: {price_discounted_ticket:.2f}lv (using card {card_number})", price_discounted_ticket]
            p.tickets += [discounted_ticket_data]
            p.total_from_tickets += price_discounted_ticket
            all_people += [p]


for person in sorted(all_people, key=lambda x: x.total_from_tickets, reverse=True):
    if person.total_from_tickets > 0:
        print(f"{person.full_name}")
        for ticket in sorted(person.tickets, key=lambda x: x[1], reverse=True):
            print(f"{ticket[0]}")
        print(f"total: {person.total_from_tickets:.2f}lv")
