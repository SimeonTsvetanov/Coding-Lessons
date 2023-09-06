function mask (params) {
    // MASK
    let catalogue = [];

    params.forEach(data => {
        let [product, price] = data.split(' : ');
        let letter = product[0];
        let presentLetter = catalogue.find(x => {return x.letter === letter});

        if (!presentLetter) {
            catalogue.push({'letter': letter, 'products': [{'product': product, 'price': price}]});
        } else {
            presentLetter.products.push({'product': product, 'price': price});
        }
    });

    catalogue.sort((a, b) => a.letter.localeCompare(b.letter));

    catalogue.forEach(letter => {
        console.log(`${letter.letter}`);
        letter.products.sort((a, b) => a.product.localeCompare(b.product));
        letter.products.forEach(product => {
            console.log(`  ${product.product}: ${product.price}`);
        });
    });
}

mask([
'Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10'
]);
// A
//  Anti-Bug Spray: 15
//  Apple: 1.25
//  Appricot: 20.4
// B
//  Boiler: 300
// D
//  Deodorant: 10
// F
//  Fridge: 1500
// T
//  T-Shirt: 10
//  TV: 1499

console.log('-------------------------------------');

mask([
'Omlet : 5.4',
'Shirt : 15',
'Cake : 59'
]
);
// C
//  Cake: 59
// O
//  Omlet: 5.4
// S
//  Shirt: 15
