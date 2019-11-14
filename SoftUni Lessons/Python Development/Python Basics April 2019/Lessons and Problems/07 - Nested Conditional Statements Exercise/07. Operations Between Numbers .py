n1 = int(input())
n2 = int(input())
operator = input()

total = 0
even_or_odd = None

if operator == "+":
    total = n1 + n2
elif operator == "-":
    total = n1 - n2
elif operator == "*":
    total = n1 * n2
elif operator == "/":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        total = n1 / n2
elif operator == "%":
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        total = n1 % n2

if total % 2 == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {total} - {even_or_odd}")
elif operator == "/" and n2 != 0:
    print(f"{n1} {operator} {n2} = {total:.2f}")
elif operator == "%" and n2 != 0:
    print(f"{n1} {operator} {n2} = {total}")
