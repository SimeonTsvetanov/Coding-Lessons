"""
Objects and Classes - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1733#2

SUPyF2 Objects/Classes-Lab - 03. Email

Problem:
Create class Email. The __init__ method should receive sender, receiver and a content.
It should also have a default set to False attribute called is_sent. The class should have two additional methods:
•	send() - sets the is_sent attribute to True
•	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
You will receive some emails until you receive "Stop" (separated by single space).
The first will be the sender, the second one – the receiver and the third one – the content
On the final line you will be given the indices of the sent emails separated by comma and space.
Call the send() method for the given emails. For each email call the get_info() method
Note: submit all of your code including the class

Example:
Input:
Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2

Output:
Peter says to John: Hi,John. Sent: True
John says to Peter: Hi,Peter!. Sent: False
Katy says to Lilly: Hello,Lilly. Sent: True
"""


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


all_emails = []
while True:
    command = input().split()
    if command[0] == "Stop":
        break
    email = Email(sender=command[0], receiver=command[1], content=command[2])
    all_emails += [email]

for email in list(map(int, input().split(", "))):
    all_emails[email].send()

[print(email.get_info()) for email in all_emails]


def email_another_solution():
    class Email:
        def __init__(self, sender: str, receiver: str, content: str):
            self.sender = sender
            self.receiver = receiver
            self.content = content
            self.is_sent = False

        def send(self):
            self.is_sent = True

        def get_info(self):
            return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

    emails = []

    while True:
        command = input().split()
        if command[0] == "Stop":
            break
        emails.append(Email(sender=command[0], receiver=command[1], content=command[2]))

    [emails[email].send() for email in list(map(int, input().split(", ")))]
    [print(email.get_info()) for email in emails]

