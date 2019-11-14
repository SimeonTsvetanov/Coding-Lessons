class Ticket:
	def __init__(self, destination, card_num, is_card_valid, price):
		self.destination = destination
		self.card_num = card_num
		self.is_card_valid = is_card_valid
		self.price = price


def is_valid(card):
	ticket_digits = list(map(int, card))
	ticket_digits_sum = sum(ticket_digits)

	is_card_valid = ticket_digits_sum % 7 == 0
	return is_card_valid


cards = {}

number_of_existing_cards = int(input())
for i in range(number_of_existing_cards):
	tokens = input().split(' ')
	first_name, last_name, card_num = tokens

	name = f'{first_name} {last_name}'

	if name not in cards:
		cards[name] = []

	cards[name].append(card_num)

tickets = {}


def calculate_ticket_price(city):
	return sum(list(map(ord, city))) / 100


while True:
	line = input()
	if line == 'time to leave!':
		break

	tokens = line.split(' ')
	_, first_name, last_name, destination, card_num = tokens
	name = f'{first_name} {last_name}'

	if name not in cards:
		cards[name] = []

	is_card_valid = is_valid(card_num)

	if not is_card_valid:
		print(f'card {card_num} is not valid!')

	price = calculate_ticket_price(destination)
	card_already_exists = None

	if is_card_valid and card_num not in cards[name]:
		values = list(cards.values())
		card_already_exists = bool([cards for cards in values if card_num in cards])

		if card_already_exists:
			print(f'card {card_num} already exists for another passenger!')
		else:
			print(f'issuing card {card_num}')
			cards[name].append(card_num)

	if card_already_exists:
		is_card_valid = False

	if is_card_valid and not card_already_exists:
		price *= .5

	if name not in tickets:
		tickets[name] = []

	ticket = Ticket(destination, card_num, is_card_valid, price)
	tickets[name].append(ticket)

sorted_passengers = sorted(tickets, key=lambda n: sum([t.price for t in tickets[n]]), reverse=True)
for name in sorted_passengers:
	print(f'{name}:')
	sorted_tickets = sorted(tickets[name], key=lambda t: t.price, reverse=True)
	for ticket in sorted_tickets:
		ticket_str = f'--{ticket.destination}: {ticket.price:.2f}lv'
		if ticket.is_card_valid:
			ticket_str += f' (using card {ticket.card_num})'
		print(ticket_str)

	total_ticket_price = sum([t.price for t in sorted_tickets])
	print(f'total: {total_ticket_price:.2f}lv')
