from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [s for s in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        if [s for s in self.songs if s == song]:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        song_found = [s for s in self.songs if s.name == song_name]
        if song_found:
            self.songs.remove(song_found[0])
            return f"Removed song {song_name} from album {self.name}."
        else:
            return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result
