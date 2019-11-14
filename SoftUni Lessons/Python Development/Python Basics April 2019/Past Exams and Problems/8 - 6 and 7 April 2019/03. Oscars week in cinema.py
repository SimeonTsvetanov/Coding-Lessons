film_name = input()
type_saloon = input()
count_tickets = int(input())

price = 0

if film_name == "A Star Is Born":
    if type_saloon == "normal":
        price = 7.50
    elif type_saloon == "luxury":
        price = 10.50
    elif type_saloon == "ultra luxury":
        price = 13.50
elif film_name == "Bohemian Rhapsody":
    if type_saloon == "normal":
        price = 7.35
    elif type_saloon == "luxury":
        price = 9.45
    elif type_saloon == "ultra luxury":
        price = 12.75
elif film_name == "Green Book":
    if type_saloon == "normal":
        price = 8.15
    elif type_saloon == "luxury":
        price = 10.25
    elif type_saloon == "ultra luxury":
        price = 13.25
elif film_name == "The Favourite":
    if type_saloon == "normal":
        price = 8.75
    elif type_saloon == "luxury":
        price = 11.55
    elif type_saloon == "ultra luxury":
        price = 13.95

price = price * count_tickets

print(f"{film_name} -> {price:.2f} lv.")
