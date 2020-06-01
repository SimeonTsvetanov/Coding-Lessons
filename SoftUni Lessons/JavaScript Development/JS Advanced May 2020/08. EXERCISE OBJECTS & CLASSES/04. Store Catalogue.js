function storeCatalogue(input) {
    // Mask - https://git.io/JfreS
    let catalogue = {};
    input.map(data => { catalogue[data.split(' : ')[0]] = Number(data.split(' : ')[1]); });

    let letter = ''
    Array.from(Object.keys(catalogue)).sort((a, b) => { a.localeCompare(b) || catalogue[a] - catalogue[b] }).map(product => {
        if (product[0] !== letter) {
            letter = product[0];
            console.log(product[0]);
        }
        console.log(`  ${product}: ${catalogue[product]}`);
    });
}

storeCatalogue(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
]);  // Should return:
// A
// Anti-Bug Spray: 15
// Apple: 1.25
// Appricot: 20.4
// B
// Boiler: 300
// D
// Deodorant: 10
// F
// Fridge: 1500
// T
// T-Shirt: 10
// TV: 1499


storeCatalogue(['Banana : 2',
    "Rubic's Cube : 5",
'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10'
]);  // Should return:
// B
// Banana: 2
// Barrel: 10
// P
// Pesho: 0.000001
// R
// Rali Car: 2000000
// Raspberry P: 4999
// Rolex: 100000
// Rollon: 10
// Rubic's Cube: 5
