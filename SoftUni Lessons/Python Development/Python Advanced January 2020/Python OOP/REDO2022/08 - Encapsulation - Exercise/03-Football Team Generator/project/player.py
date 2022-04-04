class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @property
    def sprint(self):
        return self.__sprint

    @property
    def dribble(self):
        return self.__dribble

    @property
    def passing(self):
        return self.__passing

    @property
    def shooting(self):
        return self.__shooting

    def __str__(self):
        return f"Player: {self.name}\nSprint: {self.sprint}\nDribble: {self.dribble}\n" \
               f"Passing: {self.passing}\nShooting: {self.shooting}"
