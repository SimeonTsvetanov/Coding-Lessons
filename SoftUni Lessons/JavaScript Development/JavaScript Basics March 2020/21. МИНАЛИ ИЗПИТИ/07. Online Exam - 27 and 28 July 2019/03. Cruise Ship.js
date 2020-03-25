function cruiseShip(params) {
    let cruise = params.shift();
    let cabin = params.shift();
    let nights = Number(params.shift());

    let prices = {
        'Mediterranean': {'standard cabin': 27.50, 'cabin with balcony': 30.20, 'apartment': 40.50},
        'Adriatic': {'standard cabin': 22.99, 'cabin with balcony': 25.00, 'apartment': 34.99},
        'Aegean': {'standard cabin': 23.00, 'cabin with balcony': 26.60, 'apartment': 39.80}
    };

    let price = prices[cruise][cabin] * nights * 4;

    if (nights > 7) {
        price *= 0.75;
    }

    console.log(`Annie's holiday in the ${cruise} sea costs ${price.toFixed(2)} lv.`);
}


cruiseShip(['Aegean', 'standard cabin', '10'])  // Expected Output:
// Annie's holiday in the Aegean sea costs 690.00 lv.

cruiseShip(['Adriatic', 'apartment', '5'])  // Expected Output:
// Annie's holiday in the Adriatic sea costs 699.80 lv.

cruiseShip(['Mediterranean', 'cabin with balcony', '12'])  // Expected Output:
// Annie's holiday in the Mediterranean sea costs 1087.20 lv.