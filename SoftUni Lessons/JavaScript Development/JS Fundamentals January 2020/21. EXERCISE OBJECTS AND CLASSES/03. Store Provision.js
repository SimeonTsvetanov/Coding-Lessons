function storeProvision(stock, order) {
    // Mask
    let store = {};

    // Using for loop with skipping two indexes to get the elements:
    for (let index = 0; index < stock.length; index += 2) {
        // Store[product] = value
        store[stock[index]] = Number(stock[index + 1]);
    }

    // using while loop and .shift() function while we have elements in the list:
    while (order.length > 0) {
        let product = order.shift();
        let value = Number(order.shift());
        product in store ? store[product] += value : store[product] = value;
    }

    for (let [product, value] of Object.entries(store)) {
        console.log(`${product} -> ${value}`);
    }
}

storeProvision(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']
);
// Should return:
// Chips -> 5
// CocaCola -> 9
// Bananas -> 44
// Pasta -> 11
// Beer -> 2
// Flour -> 44
// Oil -> 12
// Tomatoes -> 70
