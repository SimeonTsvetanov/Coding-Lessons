"""
Lists Advanced - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1732#0

SUPyF2 Lists Advanced-More-Ex. - 01. Messaging

Problem:
Write a program to calculate the winner of a car race. You will receive an list of numbers.
Each element of the list represents the time needed to pass through that step (the index).
There are going to be two cars. One of them starts from the left side and the other one starts from the right side.
The middle index of the list is the finish line. The number of elements in the list will always be odd.
Calculate the total time for each racer to reach the finish, which is the middle of the list,
and print the winner with his total time (the racer with less time). If you have a zero in the list,
you have to reduce the time of the racer that reached it by 20% (from his current time).
Print the result in the following format "The winner is {left/right} with total time: {total time}".

Example
Input:	                        Output:
29 13 9 0 13 0 21 0 14 82 12	The winner is left with total time: 53.8
Comment:
The time of the left racer is (29 + 13 + 9) * 0.8 (because of the zero) + 13 = 53.8
The time of the right racer is (82 + 12 + 14) * 0.8 + 21 = 107.4
The winner is the left racer, so we print it
"""
all_scores = [int(score) for score in input().split()]
left_car_scores = all_scores[:int(len(all_scores) / 2)]
right_car_scores = all_scores[int(len(all_scores) / 2) + 1:][::-1]


def total_result(scores_list: list):
    total = 0
    for result in scores_list:
        if result != 0:
            total += result
        else:
            total *= 0.8
    return total


def final(left_car, right_car):
    if left_car < right_car:
        winner, time = "left", left_car
    else:
        winner, time = "right", right_car
    return print(f"The winner is {winner} with total time: {time:.1f}")


final(total_result(left_car_scores), total_result(right_car_scores))
