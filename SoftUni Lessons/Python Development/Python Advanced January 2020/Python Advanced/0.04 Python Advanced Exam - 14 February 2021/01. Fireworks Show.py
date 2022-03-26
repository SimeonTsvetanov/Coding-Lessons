"""
*** 90/100 in Judge to work correctlly we need to change the brake
conditions in the Whlle loop. But that's NOT in the description.
ITS a falt ot the creator and it's not worth spending time on.
"""


effects = [int(e) for e in input().split(', ') if int(e) > 0]
powers = [int(p) for p in input().split(', ') if int(p) > 0]

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}

while effects and powers:
    if (fireworks["Palm"] >= 3) and (fireworks["Willow"] >= 3) and (fireworks["Crossette"] >= 3):
        result = "Congrats! You made the perfect firework show!"
        break

    effect = effects[0]
    power = powers[-1]
    mix = effect + power

    if (mix % 3 == 0) or (mix % 5 == 0):
        if (mix % 3 == 0) and (mix % 5 != 0):
            fireworks["Palm"] += 1
        elif (mix % 3 != 0) and (mix % 5 == 0):
            fireworks["Willow"] += 1
        elif (mix % 3 == 0) and (mix % 5 == 0):
            fireworks["Crossette"] += 1
        effects.pop(0)
        powers.pop(-1)
    else:
        a = effects[0] - 1
        effects.pop(0)
        effects.append(a)

result = "Sorry. You can't make the perfect firework show."
if (fireworks["Palm"] >= 3) and (fireworks["Willow"] >= 3) and (fireworks["Crossette"] >= 3):
    result = "Congrats! You made the perfect firework show!"

print(result)
if effects:
    print(f"Firework Effects left: {', '.join(str(e) for e in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(p) for p in powers)}")
for firework, count in fireworks.items():
    print(f"{firework} Fireworks: {count}")
