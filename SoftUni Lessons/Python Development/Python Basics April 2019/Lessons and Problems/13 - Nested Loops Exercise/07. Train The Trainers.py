people = int(input())

total_average = 0
average_score = 0
score = 0
counter = 0

while True:
    command = input()
    if command == "Finish":
        break
    for i in range(people):
        score = float(input())
        average_score += score
        total_average += score
        counter += 1
    print(f"{command} - {(average_score / people):.2f}.")
    average_score = 0

print(f"Student's final assessment is {(total_average / counter):.2f}.")
