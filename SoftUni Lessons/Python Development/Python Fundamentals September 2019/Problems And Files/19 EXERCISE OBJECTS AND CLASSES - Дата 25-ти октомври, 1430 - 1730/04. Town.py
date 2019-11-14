"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#3

SUPyF2 Objects/Classes-Exericse - 04. Town

Problem:
Create a class Town. The __init__ method should receive the name of the town. It should also have 3 more methods:
•	set_latitude(latitude) - set an attribute called latitude to the given one
•	set_longitude(longitude) - set an attribute called longitude to the given one
•	__repr__ - return representation of the object in the following string format:
"Town: {name} | Latitude: {latitude} | Longitude: {longitude}"

Example:
Test Code:
town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

Output:
Town: Sofia | Latitude: 42° 41' 51.04" N | Longitude: 23° 19' 26.94" E
"""


class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = ""
        self.longitude = ""

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

