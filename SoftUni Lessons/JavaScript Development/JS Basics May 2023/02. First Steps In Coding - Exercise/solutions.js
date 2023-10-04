/**
1.	Конвертор: USD към BGN
Напишете функция за конвертиране на щатски долари (USD) в български лева (BGN). 
Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.
Примерен вход и изход
вход	    изход		    вход	    изход		вход	    изход
(["22"])	39.50078		(["100"])	179.549		(["12.5"])	22.443625
*/
function usdToBgn(params) {
    let conversionRate = 1.79549;
    let usd = Number(params[0]);
    let bgn = usd * conversionRate;

    console.log(bgn);
}

// usdToBgn(["22"]);


/**
2.	Конвертор: от радиани в градуси
Напишете програма, която чете ъгъл в радиани (десетично число) 
и го преобразува в градуси. 
Използвайте формулата: градус = радиан * 180 / π. 
Числото π в Java програми е достъпно чрез Math.PI.
Примерен вход и изход
вход	        изход		            вход	        изход
(["3.1416"])	180.0004209182994		(["6.2832"])	360.0008418365988
*/
function radiansToDegrees(params) {
    let degree = Number(params[0]) * 180 / Math.PI;
    console.log(degree);
}

// radiansToDegrees(["3.1416"]);


/**
3.	Калкулатор депозити
Напишете програма, която изчислява каква сума ще получите в края на депозитния период 
при определен лихвен процент. Използвайте следната формула: 
сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
Вход
От конзолата се четат 3 реда:
1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
Изход
Да се отпечата на конзолата сумата в края на срока.
Примерен вход и изход
Вход	Изход	Обяснения
["200 ",
"3 ",
"5.7 "]	202.85	1. Изчисляваме натрупаната лихва: 200 * 0.057 (5.7%) = 11.40 лв.
                2. Изчисляваме лихвата за 1 месец: 11.40 лв. / 12 месеца = 0.95 лв.
                3. Общата сума е: 200 лв. + 3 * 0.95 лв. = 202.85 лв.
Вход	Изход	
["2350",
"6 ",
"7 "]	2432.25	1. Изчисляваме натрупаната лихва: 2350 * 0.07 (7%) = 164.50 лв.
                2. Изчисляваме лихвата за 1 месец: 164.50 лв. / 12 месеца = 13.7083... лв.
                3. Общата сума е: 2350 лв. + 6 * 13.7083... лв. = 202.85 лв.
*/
function depositcalculator(params) {
    let deposit = Number(params[0]);
    let periodInMonths = Number(params[1]);
    let annualIntrestRate = Number(params[2]);

    let accruerIntrest = (annualIntrestRate / 100) * deposit;
    let intrest = accruerIntrest / 12;
    let total = deposit + periodInMonths * intrest;

    console.log(total);
}

// depositcalculator(["200", "3", "5.7"]);
// depositcalculator(["2350", "6", "7"]);


/**
4.	Задължителна литература
За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. 
Понеже Жоро предпочита да играе с приятели навън, 
вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература.
Вход
От конзолата се четат 3 реда:
1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
Изход
Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
Примерен вход и изход
Вход	Изход	Обяснения
["212 ",
"20 ",
"2 "]	5.3	    Общо време за четене на книгата: 212 страници / 20 страници за час = 10.6 часа общо
                Необходимите часове на ден: 10.6 часа / 2 дни = 5.3 часа на ден

Вход	Изход	
["432 ",
"15 ",
"4 "]	7.2	    Общо време за четене на книгата: 432 страници / 15 страници за час = 28.8 часа общо
                Необходимите часове на ден: 28.8 часа / 4 дни = 7.2 часа на ден 
*/
function vacationBooksList(params){
    let countPages = Number(params[0]);
    let pagesPerHur = Number(params[1]);
    let daysLeft = Number(params[2]);

    let neededDays = (countPages / pagesPerHur) / daysLeft;
    console.log(neededDays);
}

// vacationBooksList(["212", "20", "2"]);


/** 
5.	Учебни материали
Учебната година вече е започнала и отговорничката на 10Б клас - 
Ани трябва да купи определен брой пакетчета с химикали, 
пакетчета с маркери, както и препарат за почистване на дъска. 
Тя е редовна клиентка на една книжарница, затова има намаление за нея, 
което представлява някакъв процент от общата сума. 
Напишете програма, която изчислява колко пари ще трябва да събере Ани, 
за да плати сметката, като имате предвид следния ценоразпис: 
•	Пакет химикали - 5.80 лв. 
•	Пакет маркери - 7.20 лв. 
•	Препарат - 1.20 лв (за литър)
Вход
От конзолата се четат 4 числа:
•	Брой пакети химикали - цяло число в интервала [0...100]
•	Брой пакети маркери - цяло число в интервала [0...100]
•	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
•	Процент намаление - цяло число в интервала [0...100]
Изход
Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.
Примерен вход и изход
Вход	Изход	Коментар
["2 ",
"3 ",
"4 ",
"25 "]	28.5	Цена на пакетите химикали => 2 * 5.80 = 11.60 лв.
                Цена на пакетите маркери => 3 * 7.20 = 21.60 лв.
                Цена на препарата => 4 * 1.20 = 4.80 лв.
                Цена за всички материали => 11.60 + 21.60 + 4.80 = 38.00 лв.
                25% = 0.25
                Цена с намаление = 38.00 – (38.00 * 0.25) = 28.50 лв.
Вход	Изход	Коментар
["4 ",
"2 ",
"5 ",
"13 "]	37.932	Цена на пакетите химикали => 4 * 5.80 = 23.20 лв.
                Цена на пакетите маркери => 2 * 7.20 = 14.40 лв.
                Цена на препарата => 5 * 1.20 = 6.00 лв.
                Цена за всички материали => 23.20 + 14.40 + 6.00 = 43.60 лв.
                13% = 0.13
                Цена с намаление = 43.60 – (43.60 * 0.13) = 37.932 лв.
*/
function suppliesForSchool(params) {
    let pencilPrice = 5.80;
    let markerPrice = 7.20;
    let chemicalLiterPrice = 1.20;

    let pencilCount = Number(params[0]);
    let markerCount = Number(params[1]);
    let litersChemical = Number(params[2]);
    let discount = Number(params[3]);

    let pensTotal = pencilCount * pencilPrice;
    let markersTotal = markerPrice * markerCount;
    let chemicalLitersTotal = chemicalLiterPrice * litersChemical;
    let totalPrice = pensTotal + markersTotal + chemicalLitersTotal;
    let discountedPRice = (discount / 100) * totalPrice;
    console.log(totalPrice - discountedPRice);
}

// suppliesForSchool(["2", "3", "4", "25"]);

/**
1.	Пребоядисване
Румен иска да пребоядиса хола и за целта е наел майстори. Напишете програма, 
която изчислява разходите за ремонта, предвид следните цени:
•	Предпазен найлон - 1.50 лв. за кв. метър
•	Боя - 14.50 лв. за литър
•	Разредител за боя - 5.00 лв. за литър
За всеки случай, към необходимите материали, 
Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, 
разбира се и 0.40 лв. за торбички. 
Сумата, която се заплаща на майсторите за 1 час работа, 
е равна на 30% от сбора на всички разходи за материали.
Вход
Входът се чете от конзолата и съдържа точно 4 реда:
1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
3.	Количество разредител (в литри) - цяло число в интервала [1…30]
4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
Изход
Да се отпечата на конзолата един ред:
•	"{сумата на всички разходи}"
Примерен вход и изход
Вход	Изход	Обяснения
["10 ",
"11 ",
"4 ",
"8 "]	727.09	Сума за найлон: (10 + 2) * 1.50 = 18 лв.
                Сума за боя: (11 + 10%) * 14.50 = 175.45 лв.
                Сума за разредител: 4 * 5.00 = 20.00 лв.
                Сума за торбички: 0.40 лв.
                Обща сума за материали: 18 + 175.45 + 20.00 + 0.40 = 213.85 лв.
                Сума за майстори: (213.85 * 30%) * 8 = 513.24 лв.
                Крайна сума: 213.85 + 513.24 = 727.09 лв.
["5 ",
"10 ",
"10 ",
"1 "]	286.52	Сума за найлон: (5 + 2) * 1.50 = 10.50 лв.
                Сума за боя: (10 + 10%) * 14.50 = 159.50 лв.
                Сума за разредител: 10 * 5.00 = 50.00 лв.
                Сума за торбички: 0.40 лв.
                Обща сума за материали: 10.50 + 159.50 + 50.00 + 0.40 = 220.40 лв.
                Сума за майстори: (220.40 * 30%) * 1 = 66.12 лв.
                Крайна сума: 220.40 + 66.12 = 286.52 лв.
*/
function repainting(params) {
    let protectiveNaylonPrice = 1.5;
    let protectiveNaylonCount = Number(params[0]);
    
    let paintPrice = 14.5;
    let paintLiters = Number(params[1]);

    let paintThinnerPrice = 5;
    let paintThinnerLiters = Number(params[2]);

    let hoursNeeded = Number(params[3]);

    let naylonTotal = protectiveNaylonPrice * (protectiveNaylonCount + 2);
    let paintTotal = paintPrice * (paintLiters + paintLiters * 0.1);
    let paintThinnerTotal = paintThinnerPrice * paintThinnerLiters;
    let plasticBags = 0.4;

    let totalMaterials = (naylonTotal + paintTotal + paintThinnerTotal + plasticBags);

    console.log(((totalMaterials * 0.3) * hoursNeeded) + totalMaterials);
}

// repainting(["10", "11", "4", "8"]);  // 727.09

/**
Ресторант отваря врати и предлага няколко менюта на преференциални цени: 
•	Пилешко меню –  10.35 лв. 
•	Меню с риба – 12.40 лв. 
•	Вегетарианско меню  – 8.15 лв. 
Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката). 
Цената на доставка е 2.50 лв и се начислява най-накрая.  
Вход
От конзолата се четат 3 реда:
•	Брой пилешки менюта – цяло число в интервала [0 … 99]
•	Брой менюта с риба – цяло число в интервала [0 … 99]
•	Брой вегетариански менюта – цяло число в интервала [0 … 99]
Изход
Да се отпечата на конзолата един ред:  "{цена на поръчката}"
Примерен вход и изход
Вход	Изход	Обяснения
["2 ",
"4 ",
"3 "]	116.2	Цена за пилешките менюта: 2 броя * 10.35  = 20.70
                Цена за менютата с риба: 4 броя * 12.40 = 49.60
                Цена за вегетарианските менюта: 3 броя * 8.15 = 24.45
                Обща цена на менютата: 20.70 + 49.60 + 24.45 = 94.75
                Цена на десерта: 20% от 94.75 = 18.95
                Цена на доставка: 2.50 (по условие)
                Обща цена на поръчката: 94.75 + 18.95 + 2.50 = 116.20

*/
function foodDelivery(params) {
    let chickenPrice = 10.35;
    let fishPrice = 12.40;
    let vegetarianPrice = 8.15;
    let deliveryPrice = 2.5;

    let chickenTotal = Number(params[0]) * chickenPrice;
    let fishTotal = Number(params[1]) * fishPrice;
    let vegetarianTotal = Number(params[2]) * vegetarianPrice;
    let desertTotal = (chickenTotal + fishTotal + vegetarianTotal) * 0.2

    let total = chickenTotal + fishTotal + vegetarianTotal + desertTotal + deliveryPrice;
    console.log(total);
}

// foodDelivery(["2", "4", "3"]);  // 116.2


/**
8.	Баскетболно оборудване
Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка. Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка: 
•	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
•	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
•	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
•	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
Вход
От конзолата се четe 1 ред:
•	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
Изход
Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.
Примерен вход и изход
Вход	Изход	Обяснения
["365 "]	811.76	Цена на тренировките за година: 365
Цена на баскетболните кецове: 365 – 40% = 219
Цена на баскетболен екип: 219 – 20% = 175.20
Цена на баскетболна топка: 1 / 4 от 175.20 = 43.80
Цена на баскетболни аксесоари: 1 /  5 от 43.80 = 8.76
Обща цена за екипировката: 365 + 219 + 175.20 + 43.80 + 8.76 = 811.76
*/
function basketballEquipment(params) {
    let oneYearPrice = Number(params[0]);
    let shoes = oneYearPrice * 0.6;
    let dress = shoes * 0.8;
    let ball = dress * 0.25;
    let accssesories = ball * 0.2;
    let total = oneYearPrice + shoes + dress + ball + accssesories;
    console.log(total);
}

// basketballEquipment(["365"]);  // 811.76


/**
9.	Аквариум
За рождения си ден Любомир получил аквариум с формата на паралелепипед. 
Първоначално прочитаме от конзолата на отделни редове размерите му 
– дължина, широчина и височина в сантиметри. 
Трябва да се пресметне колко литра вода ще събира аквариума, 
ако се знае, че определен процент от вместимостта му е заета от пясък, растения, нагревател и помпа. 
Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/. 
Да се напише програма, която изчислява литрите вода, която са необходими за напълването на аквариума.
Вход
От конзолата се четат 4 реда:
1.	Дължина в см – цяло число в интервала [10 … 500]
2.	Широчина в см – цяло число в интервала [10 … 300]
3.	Височина в см – цяло число в интервала [10… 200]
4.	Процент  – реално число в интервала [0.000 … 100.000]
Изход
Да се отпечата на конзолата едно число:
•	литрите вода, които ще събира аквариума.
Примерен вход и изход
Вход	Изход	    Обяснения
["85 ",
"75 ",
"47 ",
"17 "]	248.68875	обем на аквариумa: 85 * 75 * 47 = 299625 см3
                    обем в литри: 299625 * 0.001 или  299625 / 1000 => 299.625 литра
                    заето пространство: 17% = 0.17
                    нужни литри: 299.625 * (1 - 0.17) = 248.68875 литра
Вход	    Изход	    Обяснения
["105 ",
"77 ",
"89 ",
"18.5 "]	586.445475	обем на аквариумa: 105 * 77 * 89 = 719565 см3
                        обем в литри: 719565 * 0.001  или 719565 / 1000 => 719.565 литра
                        заето пространство: 18.5% = 0.185
                        нужни литри: 719.565 * (1 - 0.185) = 586.445475 литра
*/

function fishTank(params) {
    let length = Number(params[0]);
    let width = Number(params[1]);
    let height = Number(params[2]);
    let takenArea = Number(params[3]);

    let area = length * width * height;
    areaLiters = area / 1000;

    let neededLiters = areaLiters - (areaLiters * (takenArea / 100));
    console.log(neededLiters);
}

fishTank(["85", "75", "47", "17"])  // 248.68875
fishTank(["105", "77", "89", "18.5"]);  // 586.445475