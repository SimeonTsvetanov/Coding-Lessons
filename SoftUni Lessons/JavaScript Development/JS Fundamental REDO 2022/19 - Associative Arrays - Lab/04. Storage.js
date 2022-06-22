function storage (data) {
    // MasK
    let products = {};

    data.forEach(entry => {
        let product = entry.split(' ')[0];
        let quantity = Number(entry.split(' ')[1]);

        products.hasOwnProperty(product) ? products[product] += quantity : products[product] = quantity;
    });

    for (const [product, quantity] of Object.entries(products)) {
        console.log(`${product} -> ${quantity}`);
    }
}

storage(['tomatoes 10',
    'coffee 5',
    'olives 100',
    'coffee 40']
);

// tomatoes -> 10
// coffee -> 45
// olives -> 100
