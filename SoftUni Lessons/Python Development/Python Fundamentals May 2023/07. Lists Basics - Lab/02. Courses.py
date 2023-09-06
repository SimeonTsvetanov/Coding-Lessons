# On the first line, you will receive a single number n
n = int(input())

# On the following n lines, you will receive names of courses
# You should create a list of courses.

courses = []

for line in range(n):
    courses.append(input())

# And print it.
print(courses)
