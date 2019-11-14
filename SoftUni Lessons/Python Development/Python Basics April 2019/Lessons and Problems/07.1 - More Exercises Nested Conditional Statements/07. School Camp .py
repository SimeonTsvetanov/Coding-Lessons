season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

price = 0
sport = None

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price = 9.6 * count_nights * count_students
    elif group_type == "mixed":
        price = 10 * count_nights * count_students
    if group_type == "boys":
        sport = "Judo"
    elif group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price = 7.2 * count_nights * count_students
    elif group_type == "mixed":
        price = 9.5 * count_nights * count_students
    if group_type == "boys":
        sport = "Tennis"
    elif group_type == "girls":
        sport = "Athletics"
    elif group_type == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price = 15 * count_nights * count_students
    elif group_type == "mixed":
        price = 20 * count_nights * count_students
    if group_type == "boys":
        sport = "Football"
    elif group_type == "girls":
        sport = "Volleyball"
    elif group_type == "mixed":
        sport = "Swimming"

if count_students >= 50:
    price -= price * 0.5
elif 20 <= count_students < 50:
    price -= price * 0.15
elif 10 <= count_students < 20:
    price -= price * 0.05

print(f"{sport} {price:.2f} lv.")
