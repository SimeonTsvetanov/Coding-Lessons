from math import floor

income = float(input())
score = float(input())
wage = float(input())

social = 0
excellent = 0

if income < wage and score > 4.5:
    social = wage * 0.35

if score >= 5.5:
    excellent = score * 25

if social == 0 and excellent == 0:
    print("You cannot get a scholarship!")
elif social > excellent:
    print(f"You get a Social scholarship {floor(social)} BGN")
else:
    print(f"You get a scholarship for excellent results {floor(excellent)} BGN")




