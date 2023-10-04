def find_parentheses(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == "(":
            stack.append(i)
        elif char == ")":
            start_index = stack.pop()
            yield expression[start_index:i + 1]


expression = input()

for paren in find_parentheses(expression):
    print(paren)
