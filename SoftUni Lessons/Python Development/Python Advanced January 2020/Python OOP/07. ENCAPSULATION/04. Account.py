class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        """if the given pin is correct, return the id, otherwise return 'Wrong pin' """
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"

    def get_balance(self):
        """returns the balance"""
        return self.balance

    def change_pin(self, old_pin, new_pin):
        """if the old pin is correct, change it to the new one and return 'Pin changed', otherwise return 'Wrong pin'"""
        if self.__pin == old_pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.get_balance())
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
