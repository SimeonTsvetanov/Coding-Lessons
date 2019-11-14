total_days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0


for day in range(1, total_days + 1):
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    patients = int(input())
    if patients <= doctors:
        treated_patients += patients
    elif patients > doctors:
        untreated_patients += patients - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
