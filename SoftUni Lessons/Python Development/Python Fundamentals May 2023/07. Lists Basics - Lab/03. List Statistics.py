# On the first line, you will receive a number n
n = int(input())

# On the following n lines, you will receive integers. You should create
# • One with all the positives (including 0) numbers
positives = []
# • One with all the negatives numbers
negatives = []

for line in range(n):
    integer = int(input())
    positives.append(integer) if integer >= 0 else negatives.append(integer)

# And print two lists:
print(positives), print(negatives)

# Finally, print the following message:
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

