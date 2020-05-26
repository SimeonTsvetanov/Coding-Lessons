function populationInTowns(input) {
    // Mask
    let towns = {};
    for (let data of input) {
        let [town, population] = data.split(' <-> ');
        towns.hasOwnProperty(town) ? towns[town] += Number(population) : towns[town] = Number(population);
    }
    Object.entries(towns).map(([town, population]) => console.log(`${town} : ${population}`));
}

populationInTowns(['Sofia <-> 1200000',
    'Montana <-> 20000',
    'New York <-> 10000000',
    'Washington <-> 2345000',
    'Las Vegas <-> 1000000']
);
// Should return:
// Sofia : 1200000
// Montana : 20000
// New York : 10000000
// Washington : 2345000
// Las Vegas : 1000000

populationInTowns(['Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000']
);  // Should return:
// Istanbul : 101000
// Honk Kong : 2100004
// Jerusalem : 2352344
// Mexico City : 23401925
