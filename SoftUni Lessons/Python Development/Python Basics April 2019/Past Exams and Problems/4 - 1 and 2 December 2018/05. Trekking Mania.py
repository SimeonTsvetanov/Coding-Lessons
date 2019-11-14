groups = int(input())
total_people = 0

musala = 0
monblan = 0
kalimandjaro = 0
k2 = 0
everest = 0

for i in range(groups):
    people = int(input())
    total_people += people
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kalimandjaro += people
    elif 26 <= people <= 40:
        k2 += people
    elif people > 40:
        everest += people

print(f"{(musala / total_people * 100):.2f}%")
print(f"{(monblan / total_people * 100):.2f}%")
print(f"{(kalimandjaro / total_people * 100):.2f}%")
print(f"{(k2 / total_people * 100):.2f}%")
print(f"{(everest / total_people * 100):.2f}%")
