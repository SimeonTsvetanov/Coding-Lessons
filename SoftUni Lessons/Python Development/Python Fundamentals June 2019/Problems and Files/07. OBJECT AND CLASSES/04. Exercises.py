"""
Objects and Classes
Check your solution: https://judge.softuni.bg/Contests/Practice/Index/950#3

SUPyF Objects and Classes - 04. Exercises

Problem:
Exercises are fun … Especially when they represent a problem from your exercises.
Implement a class Exercise, which has a topic (string), a course_name (string), a judge_contest_link (string),
and problems (collection of strings).
You will receive several input lines containing information about a single exercise in the following format:
{topic} -> {course_name} -> {judge_contest_link} -> {problem1}, {problem2}. . .
You need to store every exercise in a Collection of Exercises. When you receive the command “go go go”, you end the input sequence.
You must print every exercise, in the following format:
“Exercises: {topic}
 Problems for exercises and homework for the "{course_name}" course @ SoftUni.
 Check your solutions here: {judge_contest_link}
 1. {problem1}
 2. {problem2}
 . . .”

Examples:
Input:
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go

Output:
Exercises: ObjectsAndSimpleClasses
Problems for exercises and homework for the "ProgrammingFundamentalsExtended" course @ SoftUni.
Check your solutions here: https://judge.softuni.bg/Contests/439
1. Exercises
2. OptimizedBankingSystem
3. Animals
4. Websites
5. Boxes
6. BoxIntersection
7. Messages
"""


class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


all_exercises = []
while True:
    inp = input()
    if inp == "go go go":
        break
    data = [item for item in inp.split(" -> ")]
    topic_ = data[0]
    course_name_ = data[1]
    j_c_l = data[2]
    problems_ = [item for item in data[3].split(", ")]
    a = Exercise(topic_, course_name_, j_c_l, problems_)
    all_exercises += [a]


for exercise in all_exercises:
    print(f"Exercises: {exercise.topic}")
    print(f"Problems for exercises and homework for the \"{exercise.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {exercise.judge_contest_link}")
    counter = 1
    for problem in exercise.problems:
        print(f"{counter}. {problem}")
        counter += 1
