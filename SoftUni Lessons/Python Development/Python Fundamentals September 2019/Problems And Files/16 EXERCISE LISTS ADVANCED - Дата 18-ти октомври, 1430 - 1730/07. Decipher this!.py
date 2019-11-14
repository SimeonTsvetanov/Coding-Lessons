"""
Lists Advanced - Exercise
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1731#5

SUPyF2 Lists-Advanced-Exercise - 07. Decipher this!

Problem:
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
For each word:
•	the second and the last letter are switched (e.g. Hello becomes Holle)
•	the first letter is replaced by its character code (e.g. H becomes 72)
Example:
Input:                  Output:
72olle 103doo 100ya	    Hello good day
82yade 115te 103o	    Ready set go
"""
coded_list = input().split()

for code in coded_list:
    new_word = chr(int("".join([num for num in code if num.isdigit()])))
    the_rest = [letter for letter in code if letter.isalpha()]
    if len(the_rest) > 1:
        the_rest[0], the_rest[-1] = the_rest[-1], the_rest[0]
        new_word += "".join(the_rest)
    else:
        new_word += the_rest[0]
    print(new_word, end=" ")



