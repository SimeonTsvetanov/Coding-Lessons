function storage(input) {
    // Mask
    let products = new Map();

    for (let product of input) {
        let [name, value] = product.split(' ');
        if (products.has(name)) {
            products.set(name, products.get(name) + +value);
        } else {
            products.set(name, +value);
        }
    }

    for (let [product, value] of Array.from(products.entries())) {
        console.log(`${product} -> ${value}`);
    }
}

storage(['tomatoes 10', 'coffee 5', 'olives 100', 'coffee 40']);
// Should return:
// tomatoes -> 10
// coffee -> 45
// olives -> 100
