class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        """
        :param item: adds the item in the inventory if there is space for it
        :return: Otherwise, returns "not enough room in the inventory"
        """
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self) -> int:
        """
        :return: returns the value of __capacity
        """
        return self.__capacity

    def __repr__(self) -> str:
        """
        :return: returns "Items: {items}.\nCapacity left: {left_capacity}".
        The items should be separated by ", "
        """
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
