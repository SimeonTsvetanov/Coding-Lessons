def flights(*data):
    all_flights = {}
    for i in range(0, len(data), 2):
        if data[i] == "Finish":
            break
        if data[i] not in all_flights:
            all_flights[data[i]] = 0
        all_flights[data[i]] += int(data[i + 1])
    return all_flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
