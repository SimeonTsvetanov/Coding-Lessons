from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        it_exist = [p for p in self.pokemons if p.name == pokemon.name]
        if it_exist:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        it_exist = [p for p in self.pokemons if p.name == pokemon_name]
        if it_exist:
            self.pokemons.remove(it_exist[0])
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result += f"- {p.pokemon_details()}\n"
        return result[:-1]
