"""
Create a RandomList class that has all the functionality of an List.
Add additional function that returns and removes a random element from the list.
•	Public method: get_random_element()
"""


class RandomList(list):
    def get_random_element(self):
        import random
        element = random.choice(self)
        self.remove(element)
        return element
