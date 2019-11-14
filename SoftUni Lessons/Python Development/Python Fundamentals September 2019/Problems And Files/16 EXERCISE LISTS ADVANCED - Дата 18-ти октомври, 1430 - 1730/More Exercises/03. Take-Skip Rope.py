"""
Lists Advanced - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1732#3

SUPyF2 Lists Advanced-More-Ex. - 04. Social Distribution

Problem:
Write a program, which reads a string and skips through it, extracting a hidden message.
The algorithm you have to implement is as follows:
Let’s take the string “skipTest_String044170” as an example.
Take every digit from the string and store it somewhere. After that, remove all the digits from the string.
After this operation, you should have two lists of items: the numbers list and the non-numbers list:
•	Numbers list: [0, 4, 4, 1, 7, 0]
•	Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
After that, take every digit in the numbers list and split it up into a take list and a skip list,
depending on whether the digit is in an even or an odd index:
•	Numbers list: [0, 4, 4, 1, 7, 0]
•	Take list: [0, 4, 7]
•	Skip list: [4, 1, 0]
Afterwards, iterate over both of the lists and skip {skipCount} characters from the non-numbers list,
then take {takeCount} characters and store it in a result string.
Note that the skipped characters are summed up as they go.
The process would look like this on the aforementioned non-numbers list:
1.	Take 0 characters  Taken: "", skip 4 characters (total 0)  Skipped: "skipTest_String" Result: ""
2.	Take 4 characters Taken: "Test", skip 1 characters (total 4)  Skipped: "skip"  Result: "Test"
3.	Take 7 characters Taken: "String", skip 0 characters (total 9) Skipped: ""  Result: "TestString"
After that, just print the result string on the console.
Input
•	First line: The encrypted message as a string
Output
•	First line: The decrypted message as a string
Constraints
•	The count of digits in the input string will always be even.
•	The encrypted message will contain any printable ASCII character.
Examples
Input	                                                    Output
T2exs15ti23ng1_3cT1h3e0_Roppe	                            TestingTheRope
O{1ne1T2021wf312o13Th111xreve!!@!	                        OneTwoThree!!!
this forbidden mess of an age rating 0127504740	            hidden message
"""
string_input = [symbol for symbol in input()]
numbers_list = [int(symbol) for symbol in string_input if symbol.isdigit()]
non_numbers_list = [symbol for symbol in string_input if not symbol.isdigit()]
taken = []

for num in range(0, len(numbers_list), 2):
    take = numbers_list[num]
    skip = numbers_list[num + 1]
    taken += non_numbers_list[:take]
    del non_numbers_list[:take]
    del non_numbers_list[:skip]

print("".join(taken))






