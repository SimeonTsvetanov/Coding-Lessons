from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    def add_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        found = [pl for pl in self.players if pl.name == player_name]
        if not found:
            return f"Player {player_name} not found"
        self.players.remove(found[0])
        return found[0]

