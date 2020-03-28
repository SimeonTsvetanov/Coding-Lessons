function newHouse(...input) {
    let flower = input.shift();
    let count = Number(input.shift());
    let budget = Number(input.shift());

    let price = 0;

    switch(flower) {
        case "Roses":
            if (count <= 80) {
                price = 5 * count;
            } else {
                price = (5 * count) * 0.9;
            }
            break;
        case "Dahlias":
            if (count <= 90) {
                price = 3.80 * count;
            } else {
                price = (3.80 * count) * 0.85;
            }
            break;
        case "Tulips":
            if (count <= 80) {
                price = 2.80 * count;
            } else {
                price = (2.80 * count) * 0.85;
            }
            break;
        case "Narcissus":
            if (count < 120) {
                price = (3 * count) * 1.15;
            } else {
                price = 3 * count;
            }
            break;
        case "Gladiolus":
            if (count < 80) {
                price = (2.50 * count) * 1.2;
            } else {
                price = 2.50 * count;
            }
    }

    if (price <= budget) {
        console.log(`Hey, you have a great garden with ${count} ${flower} and ${(budget -price).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money, you need ${(price - budget).toFixed(2)} leva more.`);
    }
}

newHouse(['Roses', '55', '250']);  // Expected output:
// Not enough money, you need 25.00 leva more.

newHouse(['Tulips', '88', '260']);  // Expected output:
// Hey, you have a great garden with 88 Tulips and 50.56 leva left.

newHouse(['Narcissus', '119', '360']);  // Expected output:
// Not enough money, you need 50.55 leva more.
