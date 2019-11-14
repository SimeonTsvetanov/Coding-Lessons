"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1511#3

SUPyF Exam 10.03.2019 - 04. Listmons Monsters

Problem:
Input / Constraints
An evil genius never works alone.  Listmon has own army. He wants to start tracking data for his army.
You have been asked to create a data base for Listmon's monsters.
A basic monster will always  have:
•	name -  string of any asci character without space and comma
•	id  – integer number
•	strength - integer point number
•	ugliness - integer number
In his army he accepts only two types of monsters: Hydralisks and Zerglings.
Both types has the same parameters as a basic monsters but also:
•	Hydralisk has another property – range - string of any asci character without space and comma
•	Zergling has another property – speed – integer number
Listmon does not get in his army basic monsters. They must be one of the two types mentioned above.
You will start receiving input data in format:
* Hydralisk({name}, {id}, {strength}, {ugliness}, {range})
-if there is no fifth parameter you should print '__init__() missing 1 required positional argument: 'range''
-if the fifth parameter is not a string you should print 'Range must be string'
In both cases you do not add the monster in DB
* Zergling({name}, {id}, {strength}, {ugliness}, {speed})
-if there is no fifth parameter you should print '__init__() missing 1 required positional argument: 'speed''
-if the fifth parameter is not a string you should print 'Speed must be integer’
In both cases you do not add the monster in DB
Is it possible a basic monster to try to apply in the army. If you receive a command:
*BasicMonster({name}, {id}, { strength }, {ugliness})
You must print ‘Can't instantiate abstract class BaseMonster with abstract methods __init__’
and you must  not add it in the DB.


Output
When you receive a command ‘stopAddingArmy’ you must print the information about the army in the following format:

	Overall speed of army: {speed}
	Overall strength: {strength}
	Hydralisk: {count}; Zergling: {count}
Where {speed} is the sum of all Zerglings monsters speed in DB;
{strength} is the sum of strength of all monsters;
{count} is the number of all Hydralisks/Zerglings in the DB


Examples

Input:
Zergling('Pesho', 10, 10, 10, 10)
Zergling('Pesho', 10, 10, 10, 20)
Hydralisk('a', 100, 100, 100, 'min')
Zergling('Pesho', 10, 10, 10, 30)
stopAddingArmy

Output:
Overall speed of army: 60
Overall stength: 130
Hydralisk: 1; Zergling: 3

Input:
BaseMonster('A12', 150, 200, 300)
Zergling('Pesho', 10, 10, 10, 'min')
Hydralisk('a', 100, 100, 100, 10)
Zergling('Pesho', 10, 10, 10)
Hydralisk('a', 100, 100, 100)
stopAddingArmy

Output:
Can't instantiate abstract class BaseMonster with abstract methods __init__
Speed must be integer
Range must be string
__init__() missing 1 required positional argument: 'speed'
__init__() missing 1 required positional argument: 'range'
Overall speed of army: 0
Overall stength: 0
Hydralisk: 0; Zergling: 0
"""

from abc import ABC, abstractmethod


class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name: str, id_: int, strength: int, ugliness: int):
        self.name = str(name)
        self.id_ = int(id_)
        self.strength = int(strength)
        self.ugliness = int(ugliness)


class Hydralisk(BaseMonster):
    def __init__(self, name, id_, strength, ugliness, range):
        BaseMonster.__init__(self, name, id_, strength, ugliness)
        self.range = range

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        if not isinstance(value, str):
            raise Exception('Range must be string')
        else:
            self.__range = value


class Zergling(BaseMonster):
    def __init__(self, name, id_, strength, ugliness, speed):
        BaseMonster.__init__(self, name, id_, strength, ugliness)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int):
            raise Exception('Speed must be integer')
        else:
            self.__speed = value


overall_speed_of_army = 0
overall_strength = 0
count_hydralisk = 0
count_zergling = 0

while True:
    data = input()
    if data == "stopAddingArmy":
        break
    try:
        monster = eval(data)
        overall_strength += int(monster.strength)
        if monster.__class__.__name__ == "Hydralisk":
            count_hydralisk += 1
        elif monster.__class__.__name__ == "Zergling":
            count_zergling += 1
            overall_speed_of_army += int(monster.speed)
    except Exception as e:
        print(e)

print(f"Overall speed of army: {overall_speed_of_army}")
print(f"Overall stength: {overall_strength}")
print(f"Hydralisk: {count_hydralisk}; Zergling: {count_zergling}")
