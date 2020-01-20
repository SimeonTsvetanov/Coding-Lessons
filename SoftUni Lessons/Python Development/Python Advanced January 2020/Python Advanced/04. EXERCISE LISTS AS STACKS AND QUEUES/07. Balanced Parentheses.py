# This is the solution from in class:
parentheses = input()
stack = []

pairs = {
    '{': '}',
    '[': ']',
    '(': ')'
}

valid = True

for el in parentheses:
    if el in "{([":
        stack.append(el)
    elif el in "})]":
        if stack:
            current = stack[-1]
            if pairs[current] == el:
                stack.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break

if valid:
    print("YES")
else:
    print("NO")
