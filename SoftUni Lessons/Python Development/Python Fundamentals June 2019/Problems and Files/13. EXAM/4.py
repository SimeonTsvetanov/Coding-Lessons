from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, id: str, operating_system: str, price: float):
        self.id = id
        self.operating_system = operating_system
        self.price = float(price)

    def __str__(self):
        return f"Item id: {self.id}\nOperating system: {self.operating_system}\nPrice: {self.price:.0f}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if len(value) >= 8 and value.isalpha():
            self.__id = value
        else:
            raise Exception("Invalid id!")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise Exception("Invalid price!")


class Phone(Item, ABC):
    @abstractmethod
    def __init__(self, id, operating_system, price):
        Item.__init__(self, id, operating_system, price)

    @staticmethod
    def make_call():
        return "Making call..."

    @staticmethod
    def receive_call():
        return "Receiving a call!"

    @staticmethod
    def send_message():
        return "Sending message..."

    @staticmethod
    def receive_message():
        return "Receiving a message!"


class SmartPhone(Phone):
    def __init__(self, id, operating_system, price, apps: []):
        Phone.__init__(self, id, operating_system, price)
        self.apps = apps

    @property
    def apps(self):
        return self.__apps

    @apps.setter
    def apps(self, value):
        if len(value) >= 5:
            self.__apps = value
        else:
            raise Exception("Invalid number of applications!")

    @staticmethod
    def browse_internet():
        return "Browsing..."

    def __str__(self):
        return f"Item id: {self.id}\nOperating system: {self.operating_system}\nPrice: {self.price}\nApplications: {', '.join(self.apps)}"


class CellPhone(Phone):
    def __init__(self, id, operating_system, price):
        Phone.__init__(self, id, operating_system, price)


class Tablet(Item):
    def __init__(self, id, operating_system, price):
        Item.__init__(self, id, operating_system, price)

    @staticmethod
    def browse_internet():
        return "Browsing..."

    @staticmethod
    def stream_movie():
        return "Streaming movie..."


data_base = []


while True:
    command = input()
    if command == "end":
        break
    try:
        item = eval(command)
        data_base += [item]
    except Exception as ex:
        print(ex)

while True:
    command = input()
    if command == "end":
        break
    data = command.split()
    if data[0] == "test":
        item_id = data[1]
        function = data[2]

        item_is_in_the_data_base = False
        for item in data_base:
            if item.id == item_id:
                item_is_in_the_data_base = True
                if function == "make_call()" and (item.__class__.__name__ == "SmartPhone" or item.__class__.__name__ == "SmartPhone"):
                    print(f"- Making call...")
                elif function == "receive_call()" and (item.__class__.__name__ == "SmartPhone" or item.__class__.__name__ == "SmartPhone"):
                    print(f"- Receiving a call!")
                elif function == "send_message()" and (item.__class__.__name__ == "SmartPhone" or item.__class__.__name__ == "SmartPhone"):
                    print(f"- Sending message...")
                elif function == "receive_message()" and (item.__class__.__name__ == "SmartPhone" or item.__class__.__name__ == "SmartPhone"):
                    print(f"- Receiving a message!")
                elif function == "browse_internet()" and (item.__class__.__name__ == "SmartPhone" or item.__class__.__name__ == "Tablet"):
                    print(f"- Browsing...")
                elif function == "stream_movie()" and item.__class__.__name__ == "Tablet":
                    print(f"- Streaming movie...")

        if not item_is_in_the_data_base:
            print(f"Invalid request has been made!")
    elif data[0] == "report":
        kind = data[1]
        if kind == "SmartPhone" or kind == "CellPhone" or kind == "Tablet":

            for item in data_base:
                if str(item.__class__.__name__) == kind:
                    print(item)
        else:
            print("Invalid request has been made!")

