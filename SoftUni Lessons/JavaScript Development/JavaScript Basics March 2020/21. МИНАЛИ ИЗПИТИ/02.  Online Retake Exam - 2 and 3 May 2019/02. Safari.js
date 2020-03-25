function safari(params) {
    let budget = Number(params.shift());
    let price = ((Number(params.shift()) * 2.10) + 100) * {"Saturday": 0.9, "Sunday": 0.8}[params.shift()];

    if (budget >= price) {
        console.log(`Safari time! Money left: ${(budget - price).toFixed(2)} lv.`);
    } else {
        console.log(`Not enough money! Money needed: ${(price - budget).toFixed(2)} lv.`);
    }
}

safari(['1000', '10', 'Sunday']);  // Expected Output:
// Safari time! Money left: 903.20 lv.

safari(['120', '30', 'Saturday']);  // Expected Output:
// Not enough money! Money needed: 26.70 lv.

safari(['105.20', '15', 'Sunday']);  // Expected Output:
// Safari time! Money left: 0.00 lv.
