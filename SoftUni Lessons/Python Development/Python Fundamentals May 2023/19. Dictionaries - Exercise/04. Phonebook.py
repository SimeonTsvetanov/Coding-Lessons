phonebook = {}

while True:
    data = input()
    if data.isdigit():
        for i in range(int(data)):
            searched = input()
            if searched in phonebook:
                print(f"{searched} -> {phonebook[searched]}")
            else:
                print(f"Contact {searched} does not exist.")
        break
    name, number = data.split('-')
    phonebook[name] = number

