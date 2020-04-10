function energyBooster(input) {
    // Mask
    let prices = {
        "Watermelon": {'small': 56 * 2, 'big': 28.70 * 5},
        "Mango": {'small': 36.66 * 2, 'big': 19.60 * 5},
        "Pineapple": {'small': 42.10 * 2, 'big': 24.80 * 5},
        "Raspberry": {'small': 20 * 2, 'big': 15.20 * 5}
    };

    let price = prices[input.shift()][input.shift()] * Number(input.shift());

    if (price >= 400 && price <= 1000) {price *= 0.85;}
    else if (price > 1000) {price *= 0.5;}

    console.log(`${price.toFixed(2)} lv.`)
}

energyBooster(['Watermelon', 'big', 4]);  // Should return:
// 487.90 lv.

energyBooster(['Pineapple', 'small', 1]);  // Should return:
// 84.20 lv.