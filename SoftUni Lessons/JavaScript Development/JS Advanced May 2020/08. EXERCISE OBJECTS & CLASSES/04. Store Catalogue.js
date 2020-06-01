function storeCatalogue(input) {
    // Mask - https://git.io/JfreS
    let catalogue = {};
    input.map(data => { catalogue[data.split(' : ')[0]] = Number(data.split(' : ')[1]); });

    let letter = '' // Here We will keep the current letter to Print... 
    
    // The sort method doesn't require a second argument for sort by value BUT it it's for testing :).
    // First, we will create Array from the KEYS of the Catalogue.
    Array.from(Object.keys(catalogue))
        // Then we will sort the ARRAY First Alphabetically and then if the names are the same: by value
        .sort((a, b) => { return a.localeCompare(b) || catalogue[a] - catalogue[b] })
        // And the we iterate the SORTED ARRAY element by element to print it.
        .map(product => {
        // But first we will check if the letter need's to be printed: 
        if (product[0] !== letter) {
            letter = product[0];
            console.log(product[0]);
        }
        console.log(`  ${product}: ${catalogue[product]}`);  // And Finally we will print the output line.
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
