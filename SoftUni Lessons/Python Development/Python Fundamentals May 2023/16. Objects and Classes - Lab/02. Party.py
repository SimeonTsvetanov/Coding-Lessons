class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    name = input()
    if name == 'End':
        print(f"Going: {', '.join(party.people)}")
        print(f"Total: {len(party.people)}")
        break
    party.people.append(name)
