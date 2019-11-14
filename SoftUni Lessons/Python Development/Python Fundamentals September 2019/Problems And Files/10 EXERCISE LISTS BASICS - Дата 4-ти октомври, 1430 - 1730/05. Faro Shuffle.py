"""
Lists Basics - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1725#4

SUPyF2 Lists Basics Exercise - 05. Faro Shuffle

Problem:
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in
the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original
 top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]
Write a program that receives a single string (cards separated by a space) and on the second line receives a number
 of faro shuffles that have to be made. Print the state of the deck after the shuffle
Note: The length of the deck of cards will always be an even number

Example:
Input:	                    Output:
a b c d e f g h
5
                            ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
one two three four
3	                        ['one', 'three', 'two', 'four']
"""

cards = [card for card in input().split(" ")]
times_to_split = int(input())

for each_time in range(times_to_split):
    shuffled_list = []
    for (a, b) in zip(cards[:len(cards)//2], cards[len(cards)//2:]):
        shuffled_list.append(a)
        shuffled_list.append(b)
    cards = shuffled_list

print(cards)
