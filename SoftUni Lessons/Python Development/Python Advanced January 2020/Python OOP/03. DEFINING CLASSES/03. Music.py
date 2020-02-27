"""
# This is the solution from work at home:
class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def get_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'


song = Music("Title", "Artist", "Lyrics")
print(song.get_info())
print(song.play())
"""


# And this is the solution from work in class:
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def get_info(self):
        return f'This is {self.title} from {self.artist}'

    def play(self):
        return self.lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'
