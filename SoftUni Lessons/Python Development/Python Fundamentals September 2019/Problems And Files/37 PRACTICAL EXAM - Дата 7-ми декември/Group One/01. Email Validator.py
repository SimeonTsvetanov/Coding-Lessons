"""
Programming Fundamentals Final Exam - 07 December 2019 Group 1
Check your code here: https://judge.softuni.bg/Contests/1928/Programming-Fundamentals-Final-Exam-07-December-2019-Group-1
name: Email Validator
"""

email = input()

while True:
    command = input().split(" ")
    if command[0] == "Complete":
        break

    elif command[0] == "Make":
        if command[1] == "Upper":
            email = email.upper()
        elif command[1] == "Lower":
            email = email.lower()
        print(email)

    elif command[0] == "GetDomain":
        count = int(command[1])
        print(email[-count:])

    elif command[0] == "GetUsername":
        if "@" in email:
            substring = ""
            for letter in email:
                if letter == "@":
                    break
                else:
                    substring += letter
            print(substring)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command[0] == "Replace":
        char = command[1]
        email = email.replace(char, "-")
        print(email)

    elif command[0] == "Encrypt":
        encryption = " ".join([str(ord(char)) for char in email])
        print(encryption)

