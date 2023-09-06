function mask (...params) {
    // MASK
    class Shop{
        constructor() {
            this.products = {};
        }

        addProduct(product, quantity) {
            if (product in this.products) {
                this.products[product] += quantity;
            } else {
                this.products[product] = quantity;
            }
        }

        print() {
            for (const [product, quantity] of Object.entries(this.products)) {
                console.log(`${product} -> ${quantity}`);
            }
        }
    }

    let stock = params[0];
    let newS = params[1];

    let shop = new Shop();

    for (let i = 0; i < stock.length; i += 2) { shop.addProduct(stock[i], Number(stock[i + 1])); }
    for (let i = 0; i < newS.length; i += 2) { shop.addProduct(newS[i], Number(newS[i + 1])); }

    shop.print();
}

mask([
'Chips', '5', 'CocaCola', '9', 'Bananas',
'14', 'Pasta', '4', 'Beer', '2'
],
[
'Flour', '44', 'Oil', '12', 'Pasta', '7',
'Tomatoes', '70', 'Bananas', '30'
]
);
// Chips -> 5
// CocaCola -> 9
// Bananas -> 44
// Pasta -> 11
// Beer -> 2
// Flour -> 44
// Oil -> 12
// Tomatoes -> 70

console.log('-------------------------------------');

mask([
'Salt', '2', 'Fanta', '4', 'Apple', '14',
'Water', '4', 'Juice', '5'
],
[
'Sugar', '44', 'Oil', '12', 'Apple', '7',
'Tomatoes', '7', 'Bananas', '30'
]
);
// Salt -> 2
// Fanta -> 4
// Apple -> 21
// Water -> 4
// Juice -> 5
// Sugar -> 44
// Oil -> 12
// Tomatoes -> 7
// Bananas -> 30
