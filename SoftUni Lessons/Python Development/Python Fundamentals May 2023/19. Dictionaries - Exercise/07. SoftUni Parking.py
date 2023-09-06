parking = {}

for _ in range(int(input())):
    data = input().split(' ')
    if data[0] == 'register':
        username = data[1]
        license_plate = data[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif data[0] == 'unregister':
        username = data[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for username, license_plate in parking.items():
    print(f"{username} => {license_plate}")
