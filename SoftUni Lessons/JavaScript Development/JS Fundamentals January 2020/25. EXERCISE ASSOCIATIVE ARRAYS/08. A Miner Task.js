function minerTask(input) {
    // Mask
    let resources = {};

    while (true) {
        if (input.length === 0) { break; }
        let material = input.shift();
        let value = Number(input.shift());
        resources.hasOwnProperty(material) ? resources[material] += value : resources[material] = value;
    }

    for (let [material, value] of Object.entries(resources)) {
        console.log(`${material} -> ${value}`);
    }
}

minerTask(['Gold', '155', 'Silver', '10', 'Copper', '17']);
// Should return:
// Gold -> 155
// Silver -> 10
// Copper -> 17

minerTask(['gold', '155', 'silver', '10', 'copper', '17', 'gold', '15']);
// Should return:
// gold -> 170
// silver -> 10
// copper -> 17
