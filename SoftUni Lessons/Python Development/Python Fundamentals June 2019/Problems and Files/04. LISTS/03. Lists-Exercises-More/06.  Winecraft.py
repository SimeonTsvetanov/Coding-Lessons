"""
Lists
Check your answer: https://judge.softuni.bg/Contests/Practice/Index/425#5

06. * Winecraft

Problem:
You will be given a sequence of integers, which will represent grapes. On the next line,
you will be given N - an integer, indicating the growth days. You must increment every integer in the list by 1 N times.
However, if one of the grapes’ value is greater than the grape to its left and is also greater than the one to his
right, it becomes Greater grape.
The Greater grape steals the values, which would have been incremented to its neighbors, and adds them to itself,
instead of being incremented by 1 like normal. On top of that the grapes, which are neighbors of the Greater grape
are decremented by 1 (note: if any of the greater grapes’ neighboring grapes have a value of 0,
DON’T decrement it and DON’T add its value to the greater grape).
Example: If we the list 1 12 4. The element at position 1 is greater grape, because it is bigger than the elements
 on the left and on the right:
- First iteration: The Greater grape increases with 1 by default and takes 2 from its neighbors. The new list look like:
 0 15 3
- Second iteration: The Greater grape increases with 1 by default and takes only 1 from its neighbors. This is because
the grape on left is 0 and the Greater grape takes only from the left one. The list now looks like this: 0 16 2
Lesser grapes don’t get incremented when they have as neighbor Greater grape , but instead they have their values
 decremented by 1 by their neighboring Greater grapes (if there are such), therefore their values get added to the
 Greater grapes.
After you're done with the growing (processed the grapes N times), every grape which has a value, lower than N
 should be set to a value of 0 and you should not increment them or steal values from them.
The process should then repeat, again incrementing everything N times, where the Greater grapes steal from the
lesser grapes, until your list contains less than N grapes with value more than N.
After that, print the remaining grapes on the console (one line, space-separated).

Examples:

Input:                  Output:
4 4 15 4                7 24
3

Input:                  Output:
10 11 12 13 19 13       20 35 44
5

Input:                  Output:
6 7 6 2                 16 5
3
"""


def growing(grapes, n):
    for times in range(n):
        grapes_copy = grapes.copy()
        for i in range(1, len(grapes)-1):
            if grapes[i-1] < grapes[i] > grapes[i+1]:       # Classified as greater grape
                grapes[i] += 1
                if grapes[i-1] > 0:
                    grapes[i-1] -= 1
                    grapes[i] += 1
                if grapes[i+1] > 0:
                    grapes[i+1] -= 1
                    grapes[i] += 1

    # Incrementing all grapes but the greater grapes by 1
    # ______________________________________________________
        for e in range(len(grapes)):
            if grapes_copy[e] == grapes[e]:     # the value has not been changed
                if grapes[e] > 0:
                    grapes[e] += 1
    # ______________________________________________________


def solve(grapes, n):
    grapes_copy = grapes.copy()
    while len(grapes_copy) >= n:
        growing(grapes, n)
        grapes_copy = [e for e in grapes if e > n]      # filtering the list by removing the numbers less or equal to n
        for e in range(len(grapes)):
            if grapes[e] < n:
                grapes[e] = 0
    return ' '.join(map(str, grapes_copy))


def main():
    grapes = [int(e) for e in input().split()]
    n = int(input())
    print(solve(grapes, n))


if __name__ == '__main__':
    main()

