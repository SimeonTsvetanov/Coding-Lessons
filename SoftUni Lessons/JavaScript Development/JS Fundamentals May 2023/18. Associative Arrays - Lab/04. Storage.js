function mask (params) {
    // MASK
    let products = [];
    params.map(function (x) {
        let product = x.split(' ')[0];
        let quantity = Number(x.split(' ')[1]);
        if (!(product in products)) { products[product] = 0 }
        products[product] += quantity;
    });

    for (const [product, quantity] of Object.entries(products)) {
        console.log(`${product} -> ${quantity}`);
    }
}

mask(['tomatoes 10',
'coffee 5',
'olives 100',
'coffee 40']);
// tomatoes -> 10
// coffee -> 45
// olives -> 100

console.log('-------------------------------------');

mask(['apple 50',
'apple 61',
'coffee 115',
'coffee 40']);
// apple -> 111
// coffee -> 155
