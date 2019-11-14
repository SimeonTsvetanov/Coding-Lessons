"""
Simple Operations and Calculations - Exercise
01. USD to BGN
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0
Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
Закръглете резултата до 2 цифри след десетичната запетая.
Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.
"""

usd = float(input())
bgn = usd * 1.79549

print(f"{bgn:.2f}")
