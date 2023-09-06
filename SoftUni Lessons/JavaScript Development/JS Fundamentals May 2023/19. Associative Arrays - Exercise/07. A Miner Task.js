function mask (params) {
    // MASK
    let resources = {}  // { 'resource' : quantity, ... }

    for (let i = 0; i < params.length; i += 2) {
        let resource = params[i];
        let quantity = Number(params[i + 1]);
        if (!(resource in resources)) { resources[resource] = 0; }
        resources[resource] += quantity;
    }

    for (let [resource, quantity] of Object.entries(resources)) {
        console.log(`${resource} -> ${quantity}`);
    }
}

mask([
'Gold',
'155',
'Silver',
'10',
'Copper',
'17'
]);
// Gold -> 155
// Silver -> 10
// Copper -> 17

console.log('-------------------------------------');

mask([
'gold',
'155',
'silver',
'10',
'copper',
'17',
'gold',
'15'
]);
// gold -> 170
// silver -> 10
// copper -> 17
