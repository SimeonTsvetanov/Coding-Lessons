function minerTask (data) {
    // MasK
    let resources = {};

    for (let i = 0; i < data.length; i += 2) {
        let resource = data[i];
        let quantity = +data[i + 1];

        resources.hasOwnProperty(resource) ? resources[resource] += quantity : resources[resource] = quantity;
    }

    for (let [resource, quantity] of Object.entries(resources)) {
        console.log(`${resource} -> ${quantity}`);
    }
}

minerTask([
        'Gold',
        '155',
        'Silver',
        '10',
        'Copper',
        '17'
    ]
);

// Gold -> 155
// Silver -> 10
// Copper -> 17
