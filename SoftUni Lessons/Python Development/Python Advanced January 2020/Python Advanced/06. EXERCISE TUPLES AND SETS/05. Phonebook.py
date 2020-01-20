phonebook = {}

while True:
    contact = input()
    if contact == "search":
        break
    name, number = contact.split("-")
    phonebook[name] = number

while True:
    searched_name = input()
    if searched_name == "stop":
        break
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
