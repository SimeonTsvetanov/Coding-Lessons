import re
pattern = r"\!(?P<command>[A-Z][a-z][a-z]+)\!\:\[(?P<message>[a-zA-Z]{8,})\]"

for _ in range(int(input())):
    line = input()
    match = re.match(pattern, line)
    if match:
        command = match.group("command")
        message = match.group("message")
        nums = [str(ord(letter)) for letter in message]
        print(f"{command}: {' '.join(nums)}")
    else:
        print(f"The message is invalid")
