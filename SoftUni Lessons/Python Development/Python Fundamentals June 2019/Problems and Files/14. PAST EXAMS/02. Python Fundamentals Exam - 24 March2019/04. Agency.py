"""
Basics OOP Principles
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/1590#3

SUPyF Exam 24.03.2019 - 04. Agency

Problem:
Input / Constraints
Our task is to make a database for an agency which sells apartments.
A basic apartment will have:
•	id -  string
•	rooms  – integer number
•	baths - integer number
•	square_meters – floating point number
•	price – floating point number
There are only two types of apartments the agency can manage: LivingApartments and OfficeApartments.
Both types has the same parameters as a basic.
You will start receiving input data in format:
* LivingApartment(“{id}”, {rooms}, {baths }, {square_meters }, {price})
-if there is no fifth parameter you should print “__init__() missing 1 required positional argument: 'price'”
In this case you do not add the apartment in DB
* OfficeApartment(“{id}”, {rooms}, {baths }, {square_meters }, {price})
-if there is no fifth parameter you should print “__init__() missing 1 required positional argument: 'price'”
In this case you do not add the apartment in DB
Is it possible a request for basic apartment to reach the database:
*Apartment (“{id}”, {rooms}, {baths }, {square_meters }, {price})
You must print “Can't instantiate abstract class Apartment with abstract methods __str__”
and you must  not add it in the DB.

The core difference between OfficeApartments and LivingApartments is that the LivingApartment’s price is for buying and
these apartment could not be hired and the OfficeApartmnets could only be hired not bought.
When you receive the command ‘start_selling’ you should stop adding apartments to the DB.
From this moment you will start receive a commands in format:
{buy}/{rent} {id}
Where {id} is the id of the apartment that the client wants to rent/buy.
•	If the DB is not an apartment with the given id print “Apartment with id - {id} does not exist!”
•	If there is such apartment, but it is already taken print “Apartment with id - {id} is already taken!”
•	If the apartment is available but the command is ‘rent’ and the apartment is of type LivingApartment print “Apartment with id - {id} is only for selling!”
•	If the apartment is available but the command is ‘hire’ and the apartment is of type OfficeApartment print “Apartment with id - {id} is only for renting!”
•	If none of the above cases are true, then just mark the apartment as taken.

Output
When you receive ‘free’ or ‘taken’ you should stop selling apartments and make report.
•	If you have received the ‘taken’ command you should print just the taken apartments sorted first by price ascending and then by square meters descending
•	If you have received the ‘free’ command you should print just the free apartments sorted first by price descending and then by square meters ascending
In both cases you should print the sorted apartments in the following format:
{rooms} rooms place with {bathrooms} bathroom/s.
{square_meters} sq. meters for {price} lv.
Where {rooms} are the count of the rooms in the apartment, {bathrooms} are the count of bathrooms in the apartments. {square_meters} – they are its square meters and {price} is the price .

•	In case there is no apartments according the query print “No information for this query”.

Examples:
    Input:
        Apartment("00A", 2, 1, 150, 100000)
        OfficeApartment("00O", 2, 1, 500)
        LivingApartment("00L", 3, 1, 180, 100000)
        start_selling
        rent 00L
        taken
    Output:
        Can't instantiate abstract class Apartment with abstract methods __str__
        __init__() missing 1 required positional argument: 'price'
        Apartment with id - 00L is only for selling!
        No information for this query
    Input:
        OfficeApartment("00O", 2, 1, 150, 500)
        LivingApartment("00L", 3, 1, 180, 100000)
        LivingApartment("01L", 3, 1, 190, 100000)
        start_selling
        buy 00L
        buy 01L
        rent 00O
        taken
    Output:
        2 rooms place with 1 bathroom/s.
        150.0 sq. meters for 500.0 lv.
        3 rooms place with 1 bathroom/s.
        190.0 sq. meters for 100000.0 lv.
        3 rooms place with 1 bathroom/s.
        180.0 sq. meters for 100000.0 lv.
"""
# Here I have 3 different ways to solve the problem:


class Apartment:
    def __init__(self, ap_type, ids, rooms, baths, square_meters, price, available=True):
        self.ap_type = ap_type
        self.ids = ids
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self.price = float(price)
        self.available = available

    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s."+"\n"+f"{self.square_meters} sq. meters for {self.price} lv."


all_apartments = []

while True:
    a = input()
    if a == "start_selling":
        break
    else:
        a = a.split("(")
        if a[0] == "Apartment":
            print("Can't instantiate abstract class Apartment with abstract methods __str__")
            continue

        data = [letter for letter in a[1] if letter.isalnum() or letter == " " or letter == "."]
        data = ("".join(data))
        data = [item for item in data.split(" ")]
        if len(data) < 5:
            print("__init__() missing 1 required positional argument: 'price'")
            continue
        ap = Apartment(ap_type=a[0], ids=data[0], rooms=data[1], baths=data[2], square_meters=data[3], price=data[4])
        all_apartments += [ap]


def free():
    free_apartments = [apa for apa in all_apartments if apa.available]
    free_apartments = sorted(sorted(free_apartments, key=lambda xa: xa.square_meters), key=lambda xa: xa.price, reverse=True)
    if len(free_apartments) > 0:
        for x in free_apartments:
            print(x)
    else:
        print(f"No information for this query")


def taken():
    taken_apartments = [apa for apa in all_apartments if not apa.available]
    taken_apartments = sorted(sorted(taken_apartments, key=lambda xa: xa.square_meters, reverse=True), key=lambda xa: xa.price)
    if len(taken_apartments) > 0:
        for x in taken_apartments:
            print(x)
    else:
        print(f"No information for this query")


while True:
    command = input()

    if command == "free" or command == "taken":
        if command == "free":
            free()
        elif command == "taken":
            taken()
        break

    action, ap_id = command.split(" ")

    check_if_ap_in_db = False
    for apartment in all_apartments:
        if ap_id == apartment.ids:
            check_if_ap_in_db = True
            if not apartment.available:
                print(f"Apartment with id - {ap_id} is already taken!")
            elif apartment.available and action == "rent" and apartment.ap_type == "LivingApartment":
                print(f"Apartment with id - {ap_id} is only for selling!")
            elif apartment.available and action == "hire" and apartment.ap_type == "OfficeApartment":
                print(f"Apartment with id - {ap_id} is only for renting!")
            else:
                apartment.available = False
    if not check_if_ap_in_db:
        print(f"Apartment with id - {ap_id} does not exist!")


# This is the way to solve the problem with 3 classes using the abstract class:
"""
from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, ids: str, rooms: int, baths: int, square_meters: float, price: float):
        self.ids = str(ids)
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self. price = float(price)
        self.available = True

    @abstractmethod
    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."


class LivingApartment(Apartment):
    def __init__(self, ids, rooms, baths, square_meters, price):
        Apartment.__init__(self, ids, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


class OfficeApartment(Apartment):
    def __init__(self, ids, rooms, baths, square_meters, price):
        Apartment.__init__(self, ids, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


all_apartments = []

while True:
    input_data = input()
    if input_data == "start_selling":
        break
    try:
        current_apartment = eval(input_data)
        all_apartments += [current_apartment]
    except Exception as exception:
        print(exception)

while True:
    input_data = input()
    if input_data == "free" or input_data == "taken":

        if input_data == "taken":
            taken_apartments = [ap for ap in all_apartments if not ap.available]
            taken_apartments = sorted(sorted(taken_apartments, key=lambda xa: xa.square_meters, reverse=True), key=lambda xa: xa.price)
            if len(taken_apartments) > 0:
                for apartment in taken_apartments:
                    print(apartment)
            else:
                print("No information for this query")

        elif input_data == "free":
            free_apartments = [apa for apa in all_apartments if apa.available]
            free_apartments = sorted(sorted(free_apartments, key=lambda xa: xa.square_meters), key=lambda xa: xa.price, reverse=True)
            if len(free_apartments) > 0:
                for x in free_apartments:
                    print(x)
            else:
                print(f"No information for this query")
        break

    action, ap_id = input_data.split()

    try:
        selected_apartment = [ap for ap in all_apartments if ap.ids == ap_id][0]
        if not selected_apartment.available:
            print(f"Apartment with id - {ap_id} is already taken!")
        elif selected_apartment.__class__.__name__ == "LivingApartment" and action == "rent":
            print(f"Apartment with id - {ap_id} is only for selling!")

        elif selected_apartment.__class__.__name__ == "OfficeApartment" and action == "buy":
            print(f"Apartment with id - {ap_id} is only for renting!")
        else:
            selected_apartment.available = False

    except IndexError:
        print(f"Apartment with id - {ap_id} does not exist!")
"""


# This is the third variant, made by out teacher Ines Ivanova during the classes:
"""
from abc import ABC, abstractmethod
 
class Apartment(ABC):
    def __init__(self, id, rooms, baths, square_meters, price):
        self.id = id
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self.price = float(price)
        self.is_taken = False
 
    @abstractmethod
    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."
 
 
class LivingApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)
 
    def __str__(self):
        return Apartment.__str__(self)
   
   
class OfficeApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)
 
    def __str__(self):
        return Apartment.__str__(self)
 
 
data = input()
apartments_list = []
 
while not data == "start_selling":
    try:
        current_app = eval(data)
        apartments_list.append(current_app)
    except Exception as ex:
        print(ex)
 
    data = input()
 
data_list = input().split()
ids_list = list(map(lambda a: a.id, apartments_list))
 
while not (data_list[0] == "free" or data_list[0] == "taken"):
    command = data_list[0]
    id = data_list[1]
 
    if id in ids_list:
        current_app: Apartment = list(filter(lambda a: a.id == id, apartments_list))[0]
        if current_app.is_taken:
            print(f"Apartment with id - {id} is already taken!")
        elif command == "rent" and isinstance(current_app, LivingApartment):
            print(f"Apartment with id - {id} is only for selling!")
        elif command == "buy" and isinstance(current_app, OfficeApartment):
            print(f"Apartment with id - {id} is only for renting!")
        else:
            current_app.is_taken = True
    else:
        print(f"Apartment with id - {id} does not exist!")
 
 
    data_list = input().split()
 
 
if data_list[0] == 'taken':
    taken_ap_list = list(filter(lambda a: a.is_taken == True, apartments_list))
    for apartment in sorted(taken_ap_list, key=lambda a: (a.price, -a.square_meters)):
        print(apartment)
 
elif data_list[0] == 'free':
    taken_ap_list = list(filter(lambda a: a.is_taken == False, apartments_list))
    for apartment in sorted(taken_ap_list, key=lambda a: (-a.price, a.square_meters)):
        print(apartment)
 
if len(taken_ap_list) == 0:
    print("No information for this query")
"""