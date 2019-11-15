"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#6

SUPyF2 Text-Pr.-Ex. - 07. String Explosion

Problem:
Explosions are marked with '>'. Immediately after the mark, there will be an integer,
which signifies the strength of the explosion.
You should remove x characters (where x is the strength of the explosion), starting after the punch character ('>').
If you find another explosion mark ('>') while you’re deleting characters,
you should add the strength to your previous explosion.
When all characters are processed, print the string without the deleted characters.
You should not delete the explosion character – '>', but you should delete the integers, which represent the strength.

Input
You will receive single line with the string.
Output
Print what is left from the string after explosions.
Constraints
•	You will always receive a strength for the punches
•	The path will consist only of letters from the Latin alphabet, integers and the char '>'
•	The strength of the punches will be in the interval [0…9]
Examples
Input:                              Output:
abv>1>1>2>2asdasd                   abv>>>>dasd

Input:                              Output:
pesho>2sis>1a>2akarate>4hexmaster   pesho>is>a>karate>master

Comments:
1st explosion is at index 3 and it is with strength of 1. We delete only the digit after the explosion character.
The string will look like this: abv>>1>2>2asdasd
2nd explosion is with strength one and the string transforms to this: abv>>>2>2asdasd
3rd explosion is now with strength of 2. We delete the digit and we find another explosion.
At this point the string looks like this: abv>>>>2asdasd.
4th explosion is with strength 2. We have 1 strength left from the previous explosion,
we add the strength of the current explosion to what is left and that adds up to a total strength of 3.
We delete the next three characters and we receive the string abv>>>>dasd
We do not have any more explosions and we print the result: abv>>>>dasd
"""

# This was the Initial Solution (I hate this task :D):
"""
text = [item for item in input()]
bomb = 0
i = 0
while True:
    try:
        text[i]
    except Exception:
        break
    if bomb > 0 and text[i] != ">":
        text.pop(i)
        bomb -= 1
        i -= 1
    elif text[i] == ">":
        bomb += int(text[i + 1])
    i += 1
print(''.join(text))
"""

# And this is the Solution in class:
text = input()

i = 0  # this is the index
count = 0  # This is the explosions count
result = ""  # This is the current result

while i < len(text):
    if text[i] != ">":
        result += text[i]
        i += 1
    else:
        result += ">"
        i += 1
        count += int(text[i])
        while count > 0 and text[i] != ">":
            i += 1
            count -= 1
            if i >= len(text):
                break

print(result)
