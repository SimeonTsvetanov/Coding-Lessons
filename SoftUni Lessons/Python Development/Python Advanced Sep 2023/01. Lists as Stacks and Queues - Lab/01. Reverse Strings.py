def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string


print(reverse_string(input()))
