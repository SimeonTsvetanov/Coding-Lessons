"""
Basic Syntax, Conditional Statements and Loops - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1720#2
Video: https://www.youtube.com/watch?time_continue=4&v=7sHE4HEUqi8

SUPyF2 Basic Exercise More - 03. Wolf In Sheep's Clothing

Problem:
Wolves have been reintroduced to Great Britain. You are a sheep farmer,
and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue which is at the end of the array:
[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   4      3            2      1
If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
where N is the sheep's position in the queue.
Note: there will always be exactly one wolf in the array.

Input:
The input will be a single string containing the animals separated by comma and a single space ", "

Examples:
Input:	                                        Output:
sheep, sheep, wolf	                            Please go away and stop eating my sheep
wolf, sheep, sheep, sheep, sheep, sheep	        Oi! Sheep number 5! You are about to be eaten by a wolf!
"""

text = [animal for animal in input().split(", ")]
if text[len(text) - 1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    text.reverse()
    sheep_to_be_eaten = text.index("wolf")
    print(f"Oi! Sheep number {sheep_to_be_eaten}! You are about to be eaten by a wolf!")

