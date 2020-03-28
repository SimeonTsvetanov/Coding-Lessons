function fishingBoat(...input) {
    let budget = Number(input.shift());
    let season = input.shift();
    let fishermen = Number(input.shift());

    let rent = {
        'Spring': 3000,
        'Summer': 4200,
        'Autumn': 4200,
        'Winter': 2600
    };

    let price = rent[season];

    if (fishermen <= 6) {
        price *= 0.9;
    } else if (fishermen > 6 && fishermen <= 11) {
        price *= 0.85;
    } else {
        price *= 0.75;
    }

    if (fishermen % 2 == 0 && season != "Autumn") {
        price *= 0.95;
    }

    if (budget >= price) {
        console.log(`Yes! You have ${(budget - price).toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${(price - budget).toFixed(2)} leva.`);
    }
}

fishingBoat(['3000', 'Summer', '11']);  // Expected Output:
// Not enough money! You need 570.00 leva.

fishingBoat(['3600', 'Autumn', '6']);  // Expected Output:
// Not enough money! You need 180.00 leva.

fishingBoat(['2000', 'Winter', '13']);  // Expected Output:
// Yes! You have 50.00 leva left.