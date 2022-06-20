function storeProvision (initialProducts, newProducts) {
    // MasK
    let products = {};

    let allProducts = initialProducts.concat(newProducts);
    for (let i = 0; i < allProducts.length; i += 2) {
        let product = allProducts[i];
        let value = Number(allProducts[i + 1]);

        if (!products.hasOwnProperty(product)) {
            products[product] = value
        } else {
            products[product] += value
        }
    }

    Object.entries(products).forEach(([product, value]) => {
        console.log(`${product} -> ${value}`);
    });
}

storeProvision(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']
);

// Chips -> 5
// CocaCola -> 9
// Bananas -> 44
// Pasta -> 11
// Beer -> 2
// Flour -> 44
// Oil -> 12
// Tomatoes -> 70
