function orders (product, count) {
    // MASK
    let prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    };

    console.log(`${(prices[product] * count).toFixed(2)}`);
}

orders("water", 5 );
// 5.00

orders("coffee", 2);
// 3.00
