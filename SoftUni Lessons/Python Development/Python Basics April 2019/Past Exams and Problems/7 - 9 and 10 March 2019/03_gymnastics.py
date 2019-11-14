country = input()
tool = input()

total_score = 0
score = 0

if country == "Russia":
    if tool == "ribbon":
        score = ((20 - (9.100 + 9.400)) / 20) * 100
        total_score = 9.100 + 9.400
    elif tool == "hoop":
        score = ((20 - (9.300 + 9.800)) / 20) * 100
        total_score = 9.300 + 9.800
    elif tool == "rope":
        score = ((20 - (9.600 + 9.000)) / 20) * 100
        total_score = 9.600 + 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        score = ((20 - (9.600 + 9.400)) / 20) * 100
        total_score = 9.600 + 9.400
    elif tool == "hoop":
        score = ((20 - (9.550 + 9.750)) / 20) * 100
        total_score = 9.550 + 9.750
    elif tool == "rope":
        score = ((20 - (9.500 + 9.400)) / 20) * 100
        total_score = 9.500 + 9.400
elif country == "Italy":
    if tool == "ribbon":
        score = ((20 - (9.200 + 9.500)) / 20) * 100
        total_score = 9.200 + 9.500
    elif tool == "hoop":
        score = ((20 - (9.450 + 9.350)) / 20) * 100
        total_score = 9.450 + 9.350
    elif tool == "rope":
        score = ((20 - (9.700 + 9.150)) / 20) * 100
        total_score = 9.700 + 9.150

print(f"The team of {country} get {total_score:.3f} on {tool}.")
print(f"{score:.2f}%")


