"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#0

SUPyF2 Objects/Classes-Exericse - 01. Storage

Problem:
Create a class Storage. The __init__ method should accept one parameter: the capacity of the storage.
The Storage class should also have an attribute called storage, where all the items will be stored.
The class should have two additional methods:
•	add_product(product) - adds the product in the storage if there is space for it
•	get_products() - returns the storage list
Example:
    Test Code
storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

Output:
['apple', 'banana', 'potato', 'tomato']
"""


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > 0:
            self.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())