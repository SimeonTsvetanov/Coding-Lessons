"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#4

05. * Note Statistics

Problem:
In music, certain frequencies correspond to certain musical notes (example: A -> 440hz, C# -> 554.37hz).
You will be given frequencies as real numbers on the first line of the input (space-separated).
Your task is to convert the numbers to their musical note representation,
then separate them into naturals (C, B, F and etc.) and sharp notes (C#, F#, A#, etc.).
After that, print both lists in the console in the format described in the examples.
After you print them, sum each list’s frequencies and print it on the console, rounded to the second decimal place.

Constraints
The frequencies in the input will be constrained to this chart:
Note	Frequency
C	    261.63hz
C#	    277.18hz
D	    293.66hz
D#	    311.13hz
E	    329.63hz
F	    349.23hz
F#	    369.99hz
G	    392.00hz
G#	    415.30hz
A	    440.00hz
A#	    466.16hz
B	    493.88hz
"""

all_frequencies = [float(item) for item in input().split(" ")]

notes = []
naturals = []
sharps = []
naturals_sum = 0
sharps_sum = 0

for frequency in all_frequencies:

    if frequency == 261.63:
        # C	- 261.63hz
        notes += ["C"]
        naturals += ["C"]
        naturals_sum += 261.63
    elif frequency == 277.18:
        # C# - 277.18hz
        notes += ["C#"]
        sharps += ["C#"]
        sharps_sum += 277.18
    elif frequency == 293.66:
        # D	- 293.66hz
        notes += ["D"]
        naturals += ["D"]
        naturals_sum += 293.66
    elif frequency == 311.13:
        # D# - 311.13hz
        notes += ["D#"]
        sharps += ["D#"]
        sharps_sum += 311.13
    elif frequency == 329.63:
        # E	- 329.63hz
        notes += ["E"]
        naturals += ["E"]
        naturals_sum += 329.63
    elif frequency == 349.23:
        # F	- 349.23hz
        notes += ["F"]
        naturals += ["F"]
        naturals_sum += 349.23
    elif frequency == 369.99:
        # F# - 369.99hz
        notes += ["F#"]
        sharps += ["F#"]
        sharps_sum += 369.99
    elif frequency == 392.00:
        # G	- 392.00hz
        notes += ["G"]
        naturals += ["G"]
        naturals_sum += 392.00
    elif frequency == 415.30:
        # G# - 415.30hz
        notes += ["G#"]
        sharps += ["G#"]
        sharps_sum += 415.30
    elif frequency == 440.00:
        # A	- 440.00hz
        notes += ["A"]
        naturals += ["A"]
        naturals_sum += 440.00
    elif frequency == 466.16:
        # A# - 466.16hz
        notes += ["A#"]
        sharps += ["A#"]
        sharps_sum += 466.16
    elif frequency == 493.88:
        # B - 493.88hz
        notes += ["B"]
        naturals += ["B"]
        naturals_sum += 493.88

print(f"Notes: ", end="")
for note in notes:
    print(note, end=" ")
print()

print(f"Naturals: ", end="")
print(", ".join(naturals))

print(f"Sharps: ", end="")
print(", ".join(sharps))

print(f"Naturals sum: ", end="")
print('{:.2f}'.format(naturals_sum).rstrip("0").rstrip("."))

print(f"Sharps sum: ", end="")
print('{:.2f}'.format(sharps_sum).rstrip("0").rstrip("."))


