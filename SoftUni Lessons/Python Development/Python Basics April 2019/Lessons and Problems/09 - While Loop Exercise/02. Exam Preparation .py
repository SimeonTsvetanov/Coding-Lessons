allowed_bad_scores = int(input())

tasks_counter = 0
bad_score_counter = 0
sum_score = 0
last_task = None

while bad_score_counter < allowed_bad_scores:
    task = input()
    if task == "Enough":
        sum_score = sum_score / tasks_counter
        print(f"Average score: {sum_score:.2f}")
        print(f"Number of problems: {tasks_counter}")
        print(f"Last problem: {last_task}")
        break
    score = int(input())
    sum_score += score
    tasks_counter += 1
    if score <= 4:
        bad_score_counter += 1
    last_task = task

if bad_score_counter == allowed_bad_scores:
    print(f"You need a break, {allowed_bad_scores} poor grades.")
