function mobileOperator(params) {
    let period = params.shift();
    let contract = params.shift();
    let internet = params.shift();
    let months = Number(params.shift());

    let prices = {
        'one': {'Small': 9.98, 'Middle': 18.99, 'Large': 25.98, 'ExtraLarge': 35.99},
        'two': {'Small': 8.58, 'Middle': 17.09, 'Large': 23.59, 'ExtraLarge': 31.79}
    };
    
    let price = prices[period][contract];
    if (internet == 'yes') {
        if (price <= 10) {
            price += 5.5;
        } else if (price > 10 && price <= 30) {
            price += 4.35;
        } else if (price > 30) {
            price += 3.85;
        }
    }
    if (period == "two") {
        price *= 0.9625;
    }
    price *= months;

    console.log(`${price.toFixed(2)} lv.`);
}

mobileOperator(['one', 'Small', 'yes', '10']);  // Expected Output: 154.80 lv.
mobileOperator(['two', 'Large', 'no', '10']);  // Expected Output: 227.05 lv.
mobileOperator(['two', 'ExtraLarge', 'yes', '20']);  // Expected Output: 686.07 lv.
mobileOperator(['two', 'Small', 'yes', '20']);  // Expected Output: 271.04 lv.
