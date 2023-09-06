centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = 24 * days
minutes = 60 * hours
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
