function neighborhoodsSolve(input) {
    // Mask
    let hoods = input.shift().split(', ');
    let neighborhoods = new Map();

    for (let hood of hoods) {
        neighborhoods.set(hood, []);
    }

    for (let data of input) {
        let [neighborhood, person] = data.split(' - ');
        if (neighborhoods.has(neighborhood)) {
            neighborhoods.get(neighborhood).push(person);
        }
    }

    let sorted = Array.from(neighborhoods.keys()).sort((a, b) => {
        return neighborhoods.get(b).length - neighborhoods.get(a).length;
    });

    for (let hood of sorted) {
        console.log(`${hood}: ${neighborhoods.get(hood).length}`);
        for (let person of neighborhoods.get(hood)) {
            console.log(`--${person}`);
        }
    }
}

neighborhoodsSolve([
    'Abbey Street, Herald Street, Bright Mews',
    'Bright Mews - Garry',
    'Bright Mews - Andrea',
    'Invalid Street - Tommy',
    'Abbey Street - Billy'
]);
// Should return:
// Bright Mews: 2
// --Garry
// --Andrea
// Abbey Street: 1
// --Billy
// Herald Street: 0
