function coffeMachine(params) {
    let drink = params.shift();
    let sugar = params.shift();
    let count = Number(params.shift());

    let prices = {
        'Espresso': { 'Without': 0.90, 'Normal': 1, 'Extra': 1.2 },
        'Cappuccino': { 'Without': 1, 'Normal': 1.2, 'Extra': 1.6 },
        'Tea': { 'Without': 0.5, 'Normal': 0.6, 'Extra': 0.7 }
    };

    let price = prices[drink][sugar] * count;

    if (sugar == "Without") {
        price *= 0.65;
    }
    if (drink == "Espresso" && count >= 5) {
        price *= 0.75;
    }
    if (price > 15) {
        price *= 0.8;
    }

    console.log(`You bought ${count} cups of ${drink} for ${price.toFixed(2)} lv.`);
}


coffeMachine(['Espresso', 'Without', '10']);  // Expected Output:
// You bought 10 cups of Espresso for 4.39 lv.

coffeMachine(['Cappuccino', 'Normal', '13']);  // Expected Output:
// You bought 13 cups of Cappuccino for 12.48 lv.

coffeMachine(['Tea', 'Extra', '3']);  // Expected Output:
// You bought 3 cups of Tea for 2.10 lv.