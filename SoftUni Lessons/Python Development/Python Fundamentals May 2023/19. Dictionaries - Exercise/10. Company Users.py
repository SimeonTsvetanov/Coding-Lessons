companies = {}

while True:
    command = input().split(' -> ')
    if command[0] == 'End':
        break
    company, ids = command

    if company not in companies:
        companies[company] = []
    if ids not in companies[company]:
        companies[company].append(ids)

for company, employees in companies.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")


