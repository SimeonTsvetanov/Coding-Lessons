"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1578#2

SUPyF Exam Preparation 2 - 03. Arena Tier
Problem:
Pesho is a pro gladiator, he is struggling to become master of the Arena. // TODO some more story
You will receive several input lines in one of the following formats:
"{gladiator} -> {technique} -> {skill}"
"{gladiator} vs {gladiator}"
The gladiator and technique are strings, the given skill will be an integer number.
You need to keep track of every gladiator.
When you receive a gladiator and his technique and skill, add him to the gladiator pool, if he isn`t present,
else add his technique or update his skill, only if the current technique skill is lower than the new value.
If you receive "{gladiator} vs {gladiator}" and both gladiators exist in the tier, they duel with the following rules:
Compare their techniques, if they got at least one in common,
the gladiator with better total skill points wins and the other is demoted from the tier -> remove him.
If they don`t have techniques in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Ave Cesar". At that point you should print the gladiators,
ordered by total skill in desecending order, then ordered by name in ascending order.
Foreach gladiator print their technique and skill, ordered desecending,
then ordered by technique name in ascending order
Input / Constraints
You will receive input on several lines.
•	The input comes in the form of commands in one of the formats specified above.
•	Gladiator and technique will always be one word string, containing no whitespaces.
•	Skill will be an integer in the range [0, 1000].
•	There will be no invalid input lines.
•	The programm ends when you receive the command "Ave Cesar".

Output
•	The output format for each gladiator is:
"{gladiator}: {totalSkill} skill"
"- {technique} <!> {skill}"

Scroll down to see examples.

Input:
Pesho -> BattleCry -> 400
Gosho -> PowerPunch -> 300
Stamat -> Duck -> 200
Stamat -> Tiger -> 250
Ave Cesar

Output:
Stamat: 450 skill
- Tiger <!> 250
- Duck <!> 200
Pesho: 400 skill
- BattleCry <!> 400
Gosho: 300 skill
- PowerPunch <!> 300

Input:
Pesho -> Duck -> 400
Julius -> Shield -> 150
Gladius -> Heal -> 200
Gladius -> Support -> 250
Gladius -> Shield -> 250
Pesho vs Gladius
Gladius vs Julius
Gladius vs Gosho
Ave Cesar

Output:
Gladius: 700 skill
- Support <!> 250
- Shield <!> 250
- Heal <!> 200
Pesho: 400 skill
- Duck <!> 400
"""


class Gladiator:
    def __init__(self, name: str, skills: [], total_skill_points: int):
        self.name = name
        self.skills = skills
        self.total_skill_points = total_skill_points


class Skill:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


gladiators_pool = []

while True:
    command = input()
    if command == "Ave Cesar":
        break
    if "->" in command:
        gladiator_name, skill_name, skill_value = command.split(" -> ")
        skill_value = int(skill_value)

        not_in_pool = True
        for gladiator in gladiators_pool:
            if gladiator.name == gladiator_name:

                skill_not_in_skills = True

                for skill in gladiator.skills:
                    if skill.name == skill_name:
                        skill_not_in_skills = False

                        if skill.value < skill_value:

                            old_skill_points = skill.value
                            gladiator.total_skill_points -= old_skill_points
                            gladiator.total_skill_points += skill_value

                            skill.value = skill_value

                if skill_not_in_skills:
                    gladiator.skills += [Skill(name=skill_name, value=skill_value)]
                    gladiator.total_skill_points += skill_value

                not_in_pool = False

        if not_in_pool:
            skill = Skill(name=skill_name, value=skill_value)
            gladiator = Gladiator(name=gladiator_name, skills=[skill], total_skill_points=skill_value)
            gladiators_pool += [gladiator]

    elif "vs" in command:
        gladiator_1, vs, gladiator_2 = command.split()
        for gladiator1 in gladiators_pool:
            if gladiator1.name == gladiator_1:
                for gladiator2 in gladiators_pool:
                    if gladiator2.name == gladiator_2:

                        for skill_gl_1 in gladiator1.skills:
                            for skill_gl_2 in gladiator2.skills:
                                if skill_gl_1.name == skill_gl_2.name:
                                    if gladiator1.total_skill_points > gladiator2.total_skill_points:
                                        if gladiator2 in gladiators_pool:
                                            gladiators_pool.remove(gladiator2)
                                            break
                                    elif gladiator2.total_skill_points > gladiator1.total_skill_points:
                                        if gladiator1 in gladiators_pool:
                                            gladiators_pool.remove(gladiator1)
                                            break

gladiators_pool = sorted(sorted(gladiators_pool, key=lambda x: x.name), key=lambda x: x.total_skill_points, reverse=True)

for gladiator in gladiators_pool:
    print(f"{gladiator.name}: {gladiator.total_skill_points} skill")
    for skill in sorted(sorted(gladiator.skills, key=lambda x: x.name), key=lambda x: x.value, reverse=True):
        print(f"- {skill.name} <!> {skill.value}")
