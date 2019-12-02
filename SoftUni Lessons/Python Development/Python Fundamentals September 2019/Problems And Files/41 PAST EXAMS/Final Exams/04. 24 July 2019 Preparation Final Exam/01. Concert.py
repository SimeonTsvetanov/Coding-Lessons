"""
Programming Fundamentals Final Exam Preparation - 24 July 2019
link: https://judge.softuni.bg/Contests/Practice/Index/1759#0
Name: 01. Concert
"""


class Band:
    def __init__(self, name: str, new_members=None, time=0):
        self.name = name
        self.members = []
        self.add_members(new_members)
        self.time = time

    def add_members(self, new_members):
        if new_members:
            for member in new_members:
                if member not in self.members:
                    self.members.append(member)


all_bands = []

while True:
    command = input().split("; ")
    if command[0] == "start of concert":
        break
    if command[0] == "Add":
        add_name = command[1]
        members_to_add = command[2].split(", ")
        band_is_present = False
        for band in all_bands:
            if band.name == add_name:
                band_is_present = True
                band.add_members(new_members=members_to_add)
        if not band_is_present:
            all_bands.append(Band(name=add_name, new_members=members_to_add))

    elif command[0] == "Play":
        play_band_name = command[1]
        play_time = int(command[2])
        play_band_is_present = False
        for band in all_bands:
            if band.name == play_band_name:
                play_band_is_present = True
                band.time += play_time
        if not play_band_is_present:
            all_bands.append(Band(name=play_band_name, time=play_time))

print(f"Total time: {sum([band.time for band in all_bands])}")
for band in sorted(all_bands, key=lambda x: (-x.time, x.name)):
    print(f"{band.name} -> {band.time}")

band_to_print = input()
for band in all_bands:
    if band.name == band_to_print:
        print(band.name)
        for band_member in band.members:
            print(f"=> {band_member}")

