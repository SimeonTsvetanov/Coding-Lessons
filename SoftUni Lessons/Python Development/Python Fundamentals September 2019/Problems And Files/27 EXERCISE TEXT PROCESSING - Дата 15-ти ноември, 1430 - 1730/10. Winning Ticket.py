"""
Text Processing - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1740#9

SUPyF2 Text-Pr.-Ex. - 10. Winning Ticket (not included in final score)

Problem:
Lottery is exciting. What is not, is checking a million tickets for winnings only by hand.
So, you are given the task to create a program which automatically checks if a ticket is a winner.
You are given a collection of tickets separated by commas and spaces.
You need to check every one of them if it has a winning combination of symbols.
A valid ticket should have exactly 20 characters. The winning symbols are '@', '#', '$' and '^'.
But in order for a ticket to be a winner the symbol should uninterruptedly repeat for at least 6 times in both
the tickets left half and the tickets right half.
For example, a valid winning ticket should be something like this:
"Cash$$$$$$Ca$$$$$$sh"
The left half "Cash$$$$$$" contains "$$$$$$", which is also contained in the tickets right half "Ca$$$$$$sh".
A winning ticket should contain symbols repeating up to 10 times in both halves, which is considered a Jackpot (for example: "$$$$$$$$$$$$$$$$$$$$").
Input
The input will be read from the console.
The input consists of a single line containing all tickets separated by
commas and one or more white spaces in the format:
•	"{ticket}, {ticket}, … {ticket}"
Output
Print the result for every ticket in the order of their appearance, each on a separate line in the format:
•	Invalid ticket - "invalid ticket"
•	No match - "ticket "{ticket}" - no match"
•	Match with length 6 to 9 - "ticket "{ticket}" - {match length}{match symbol}"
•	Match with length 10 - "ticket "{ticket}" - {match length}{match symbol} Jackpot!"
Constrains
•	Number of tickets will be in range [0 … 100]
Examples:
Input:
Cash$$$$$$Ca$$$$$$sh
Output:
ticket "Cash$$$$$$Ca$$$$$$sh" - 6$

Input:
$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey
Output:
ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
invalid ticket
ticket "th@@@@@@eemo@@@@@@ey" - 6@

Input:
validticketnomatch:(
Output:
ticket "validticketnomatch:(" - no match
"""
a = [''.join([letter for letter in item if letter != ' ']) for item in input().split(", ")]
for ticket in a:
    if len(ticket) == 20:
        middle = (len(ticket) + 1) // 2
        left_half = ticket[:middle]
        right_half = ticket[middle:]

        if "@@@@@@" in left_half and "@@@@@@" in right_half:
            total_times = min(left_half.count("@"), right_half.count("@"))
            if total_times == 10:
                print(f'ticket "{ticket}" - 10@ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {total_times}@')

        elif "######" in left_half and "######" in right_half:
            total_times = min(left_half.count("#"), right_half.count("#"))
            if total_times == 10:
                print(f'ticket "{ticket}" - 10# Jackpot!')
            else:
                print(f'ticket "{ticket}" - {total_times}#')

        elif "$$$$$$" in left_half and "$$$$$$" in right_half:
            total_times = min(left_half.count("$"), right_half.count("$"))
            if total_times == 10:
                print(f'ticket "{ticket}" - 10$ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {total_times}$')

        elif "^^^^^^" in left_half and "^^^^^^" in right_half:
            total_times = min(left_half.count("^"), right_half.count("^"))
            if total_times == 10:
                print(f'ticket "{ticket}" - 10^ Jackpot!')
            else:
                print(f'ticket "{ticket}" - {total_times}^')

        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'invalid ticket')
