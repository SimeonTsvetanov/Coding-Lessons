"""
Conditional Statements - Lab
Проверка: https://judge.softuni.bg/Contests/Practice/Index/1012#0

12. Toy Shop

Условие:
Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели,
иска да отиде на екскурзия. Да се напише програма, която пресмята печалбата от поръчката.
Цени на играчките:
-Пъзел - 2.60 лв.
-Говореща кукла - 3 лв.
-Плюшено мече - 4.10 лв.
-Миньон - 8.20 лв.
-Камионче - 2 лв.
Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена.
От спечелените пари Петя трябва да даде 10% за наема на магазина.
Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
Вход
От конзолата се четат 6 реда:
1.	Цена на екскурзията - реално число;
2.	Брой пъзели - цяло число;
3.	Брой говорещи кукли - цяло число;
4.	Брой плюшени мечета - цяло число;
5.	Брой миньони - цяло число;
6.	Брой камиончета - цяло число.
Изход
На конзолата се отпечатва:
-Ако парите са достатъчни се отпечатва:
-"Yes! {оставащите пари} lv left."
-Ако парите НЕ са достатъчни се отпечатва:
-"Not enough money! {недостигащите пари} lv needed."
Резултатът трябва да се форматира до втория знак след десетичната запетая.
"""

excursion_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())


total_clean = (count_puzzles * 2.6) + (count_dolls * 3) + \
              (count_bears * 4.1) + (count_minions * 8.2) + (count_trucks * 2)


total = 0
count_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

if count_toys >= 50:
    total_clean = total_clean - (total_clean * 0.25)
    total = total_clean - (total_clean * 0.10)
    if total >= excursion_price:
        difference = total - excursion_price
        print(f"Yes! {difference:.2f} lv left.")
    else:
        difference = excursion_price - total
        print(f"Not enough money! {difference:.2f} lv needed.")
elif count_toys < 50:
    total = total_clean - (total_clean * 0.10)
    if total >= excursion_price:
        difference = total - excursion_price
        print(f"Yes! {difference:.2f} lv left.")
    else:
        difference = excursion_price - total
        print(f"Not enough money! {difference:.2f} lv needed.")





