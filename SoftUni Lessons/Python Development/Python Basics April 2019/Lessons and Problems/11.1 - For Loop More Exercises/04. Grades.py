students = int(input())

n1 = 0
n2 = 0
n3 = 0
n4 = 0
total_average_score = 0


for i in range(1, students + 1):
    score = float(input())
    total_average_score += score
    if 2.00 <= score <= 2.99:
        n1 += 1
    elif 3.00 <= score <= 3.99:
        n2 += 1
    elif 4.00 <= score <= 4.99:
        n3 += 1
    elif score >= 5:
        n4 += 1

print(f"Top students: {(n4 / students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(n3 / students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(n2 / students * 100):.2f}%")
print(f"Fail: {(n1 / students * 100):.2f}%")
print(f"Average: {(total_average_score / students):.2f}")
