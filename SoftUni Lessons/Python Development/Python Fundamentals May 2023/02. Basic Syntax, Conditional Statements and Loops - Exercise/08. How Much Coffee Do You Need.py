events = ['coding', 'dog', 'cat', 'movie']
coffees = 0

while True:
    command = input()
    if command == "END":
        break
    if command.lower() in events:
        if command.islower():
            coffees += 1
        else:
            coffees += 2

if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")
