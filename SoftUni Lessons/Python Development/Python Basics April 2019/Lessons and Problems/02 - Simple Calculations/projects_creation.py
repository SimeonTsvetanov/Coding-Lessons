"""
Simple Operations and Calculations - Lab
05. Projects Creation
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1011#2
Напишете програма, която изчислява колко часове ще са необходими на един архитект, за да изготви проектите на няколко
строителни обекта. Изготвянето на един проект отнема приблизително три часа.
Вход
От конзолата се четат 2 реда:
1.	Името на архитекта - текст;
2.	Брой на проектите - цяло число.
Изход
На конзолата се отпечатва:
"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."
"""

name = input()
projects_count = int(input())

time_needed = projects_count * 3

print(f"The architect {name} will need {time_needed} hours to complete {projects_count} project/s.")
