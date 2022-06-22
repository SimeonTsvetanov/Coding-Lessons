function legendaryFarming (data) {
    // MasK
    data = data.split(' ');
    let materials = {
        'shards': 0,
        'motes': 0,
        'fragments': 0
    };
    let junk = {};
    let item = undefined;

    for (let i = 0; i < data.length; i += 2) {
        if (item) { break; }

        let newMaterial = data[i + 1].toLowerCase();
        let newValue = +data[i];

        if (materials.hasOwnProperty(newMaterial)) {
            materials[newMaterial] += newValue;
        } else {
            junk.hasOwnProperty(newMaterial) ? junk[newMaterial] += newValue : junk[newMaterial] = newValue;
        }

        if (materials["shards"] >= 250) {
            item = "Shadowmourne";
            materials["shards"] -= 250;
        } else if (materials["fragments"] >= 250) {
            item = "Valanyr";
            materials["fragments"] -= 250;
        } else if (materials["motes"] >= 250) {
            item = "Dragonwrath";
            materials["motes"] -= 250;
        }
    }

    console.log(`${item} obtained!`);
    let sortedMaterials =  Array.from(Object.entries(materials)).sort((a, b) => {
        return b[1] - a[1] || a[0].localeCompare(b[0]);
    });
    for (let [material, value] of sortedMaterials) {
        console.log(`${material}: ${value}`);
    }
    let sortedJunk =  Array.from(Object.entries(junk)).sort((a, b) => {
        return a[0].localeCompare(b[0]) || 'pass without P';
    });
    for (let [material, value] of sortedJunk) {
        console.log(`${material}: ${value}`);
    }
}
