class Wizard:
    def __init__(self, name, health: int, damage: int):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)


all_wizards = []

while True:
    command = input()
    if command == "fight":
        break
    command = command.split()
    if command[0] == "new":
        new_wizard_name = command[1]
        new_wizard_health = int(command[2])
        new_wizard_damage = int(command[3])

        wizard_already_exist = False
        for wizard in all_wizards:
            if wizard.name == new_wizard_name:
                print(f"Wizard already exists!")
                wizard_already_exist = True

        if not wizard_already_exist:
            new_wizard = Wizard(name=new_wizard_name, health=new_wizard_health, damage=new_wizard_damage)
            all_wizards += [new_wizard]

    elif command[0] == "edit":
        edit_wizard_name = command[1]
        edit_wizard_health = int(command[2])
        edit_wizard_damage = int(command[3])

        wizard_does_exist = False
        for wizard in all_wizards:
            if wizard.name == edit_wizard_name:
                wizard_does_exist = True
                wizard.health += edit_wizard_health
                wizard.damage += edit_wizard_damage
        if not wizard_does_exist:
            print(f"Wizard does not exist!")

while True:
    command = input()
    if command == "end":
        break
    fighter_1, fighter_2 = command.split(" <=> ")

    fighter_1_exists = False
    fighter_2_exists = False

    for wizard in all_wizards:
        if fighter_1 == wizard.name:
            fighter_1_exists = True
        if fighter_2 == wizard.name:
            fighter_2_exists = True

    if fighter_1_exists and fighter_2_exists:

        for attacked in all_wizards:
            if attacked.name == fighter_2:
                for attacker in all_wizards:
                    if attacker.name == fighter_1:
                        attacked.health -= attacker.damage
                        attacker.health += 50
                        if attacked.health <= 0:
                            print(f"Fatality - {attacker.name} wins!")
                            all_wizards.remove(attacked)
                        else:
                            print(f"Next time {attacked.name}!")
    else:
        print("Cannot place a fight with non-existing wizards!")


for wizard in sorted(all_wizards, key=lambda x: x.health, reverse=True):
    print(f"Wizard: {wizard.name}. Health: {wizard.health}. Damage power: {wizard.damage}")



