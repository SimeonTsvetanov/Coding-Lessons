"""
Objects and Classes - Exericse
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1734#5

SUPyF2 Objects/Classes-Exericse - 06. Inventory

Problem:
Create a class Inventory. The __init__ method should accept only the capacity of the inventory.
The capacity should be a private attribute (__capacity). You can read more about private attributes here.
Each inventory should also have an attribute called items, where all the items will be stored.
The class should also have 3 methods:
•	add_item(item) - adds the item in the inventory if there is space for it. Otherwise, returns
"not enough room in the inventory"
•	get_capacity() - returns the value of __capacity
•	__repr__() - returns "Items: {items}. Capacity left: {left_capacity}". The items should be separated by ", "

Examples:
Test Code:
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)

Output:
not enough room in the inventory
2
Items: potion, sword.
Capacity left: 0
"""


# class Inventory:
#     def __init__(self, capacity):
#         self.__capacity = capacity
#         self.items = []
#
#     def add_item(self, item):
#         if len(self.items) < self.__capacity:
#             self.items.append(item)
#             return
#         return f"not enough room in the inventory"
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)







