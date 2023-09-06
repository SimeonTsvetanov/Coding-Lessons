def to_do():
    notes = []

    while True:
        note = input().split("-")
        if note[0] == "End":
            break
        notes.append([int(note[0]), note[1]])

    print([(note[1]) for note in list(sorted(notes, key=lambda x: x[0]))])


if __name__ == '__main__':
    to_do()
