function mask (params) {
    // MASK - Unlikely the previous task. This one is good.
    let keyMaterials = { 'shards': 0, 'fragments': 0, 'motes': 0 };
    let items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'};
    let otherMaterials = {};
    let legendaryItem = false;

    params = params.split(' ');

    for (let i = 0; i < params.length; i += 2) {
        if (legendaryItem) { break; }
        let value = Number(params[i]);
        let material = params[i + 1].toLowerCase();
        if (material in keyMaterials) {
            keyMaterials[material] += value;
            if (keyMaterials[material] >= 250) {
                legendaryItem = items[material];
                keyMaterials[material] -= 250;
            }
        } else {
            if (!(material in otherMaterials)) {
                otherMaterials[material] = 0;
            }
            otherMaterials[material] += value;
        }
    }

    console.log(`${legendaryItem} obtained!`);
    for (let [material, quantity] of Object.entries(keyMaterials)
        .sort((a, b) => {
            return b[1] - a[1] || a[0].localeCompare(b[0]);
    })) { console.log(`${material}: ${quantity}`); }

    for (let [material, quantity] of Object.entries(otherMaterials)
        .sort((a, b) => {
            return a[0].localeCompare(b[0]) || 'pass without P';
    })) { console.log(`${material}: ${quantity}`); }
}

mask('3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards');
// Valanyr obtained!
// fragments: 5
// shards: 5
// motes: 3
// leathers: 6
// stones: 5

console.log('-------------------------------------');

mask('123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver');
// Dragonwrath obtained!
// shards: 22
// motes: 19
// fragments: 0
// fangs: 9
// silver: 123
