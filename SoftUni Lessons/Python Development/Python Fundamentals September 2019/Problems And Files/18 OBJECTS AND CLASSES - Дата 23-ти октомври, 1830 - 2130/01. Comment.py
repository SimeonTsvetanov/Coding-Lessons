"""
Objects and Classes - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1733#0

SUPyF2 Objects/Classes-Lab - 01. Comment

Problem:
Create a class with name "Comment". The __init__ method should accept 3 parameters
•	username
•	content
•	likes (optional, 0 by default)
Use the exact names for your variables
Note: there is no input/output for this problem. Test the class yourself and submit only the class

Example:
Test Code	                                        Output
comment = Comment("user1", "I like this book")      user1
print(comment.username)                             I like this book
print(comment.content)                              0
print(comment.likes)
"""


class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


 class Comment_take_two:
    def __init__(self, username: str, content: str, likes=0):
        self.username = username
        self.content = content
        self.likes = likes
