class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        """
        changes the name of the movie
        """
        self.name = new_name

    def change_director(self, new_director: str):
        """
        changes the director of the movie
        """
        self.director = new_director

    def watch(self):
        """
        change the watched attribute to True
        and increase the total watched movies class attribute (if the movie is not already watched)
        """
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self) -> str:
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
