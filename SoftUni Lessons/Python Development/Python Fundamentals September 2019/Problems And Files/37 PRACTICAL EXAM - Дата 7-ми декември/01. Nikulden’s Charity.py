string = input()

while True:
    command = input().split(" ")
    if command[0] == "Finish":
        break

    elif command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        string = string.replace(current_char, new_char)
        print(string)

    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= end_index <= len(string):
            start = string[0:start_index]
            end = string[end_index + 1:len(string)]
            string = start + end
            print(string)
        else:
            print(f"Invalid indexes!")

    elif command[0] == "Make":
        lower_or_upper = command[1]
        if lower_or_upper == "Lower":
            string = string.lower()
            print(string)
        elif lower_or_upper == "Upper":
            string = string.upper()
            print(string)

    elif command[0] == "Check":
        new_string = command[1]
        if new_string in string:
            print(f"Message contains {new_string}")
        else:
            print(f"Message doesn't contain {new_string}")

    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= end_index <= len(string):
            substring = string[start_index:end_index + 1]
            total = 0
            for letter in substring:
                total += ord(letter)
            print(total)
        else:
            print(f"Invalid indexes!")
