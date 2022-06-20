function orders (product, quantity) {
    // MasK
    let price = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }[product];

    console.log((price * quantity).toFixed(2));
}

orders('water', 5);  // 5.00