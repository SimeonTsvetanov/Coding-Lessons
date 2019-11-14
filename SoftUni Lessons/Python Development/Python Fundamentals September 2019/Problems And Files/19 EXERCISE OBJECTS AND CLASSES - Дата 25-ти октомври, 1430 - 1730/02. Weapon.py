"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#1

SUPyF2 Objects/Classes-Exericse - 02. Weapon


Problem:
Create a class Weapon. The __init__ method should receive an amount of bullets (integer).
The class should also have the following methods:
•	shoot() - if there are bullets in the weapon, reduce them by 1 and return a message "shooting…".
If there are no bullets left, return: "no bullets left"
You should also override the toString method, so that the following code: print(weapon) should work.
To do that define a __repr__ method that returns "Remaining bullets: {amount_of_bullets}".
You can read more about the __repr__ method here: link

Example:

Test Code:
weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)

Output:
['apple', 'banana', 'potato', 'tomato']
"""


class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __str__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
