from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @ classmethod
    def from_stars(cls, stars_count: int):
        return cls(name=f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number]
        if room:
            count = room[0].take_room(people)
            if type(count) == int:
                self.guests += count

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number]
        if room:
            count = room[0].free_room()
            if type(count) == int:
                self.guests -= count

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(list(map(str, [r.number for r in self.rooms if not r.is_taken])))}\n"
        result += f"Taken rooms: {', '.join(list(map(str, [r.number for r in self.rooms if r.is_taken])))}"
        return result

