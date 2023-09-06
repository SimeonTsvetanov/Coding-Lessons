function mask (params) {
    // MASK
    let inventory = params.shift().split(' ');

    params.forEach(data => {
        let [command, rest] = data.split(' ');

        if (command === 'Buy') {
            if (!inventory.includes(rest)) {
                inventory.push(rest);
            }
        } else if (command === 'Trash') {
            if (inventory.includes(rest)) {
                inventory.splice(inventory.indexOf(rest), 1);
            }
        } else if (command === 'Repair') {
            if (inventory.includes(rest)) {
                inventory.splice(inventory.indexOf(rest), 1);
                inventory.push(rest);
            }
        } else if (command === 'Upgrade') {
            let [equipment, upgrade] = rest.split('-');
            if (inventory.includes(equipment)) {
                inventory.splice(inventory.indexOf(equipment) + 1, 0, `${equipment}:${upgrade}`);
            }
        }
    });

    console.log(inventory.join(' '));
}

mask(['SWORD Shield Spear',
'Buy Bag',
'Trash Shield',
'Repair Spear',
'Upgrade SWORD-Steel']
);
// SWORD SWORD:Steel Bag Spear

console.log('-------------------------------------');

mask(['SWORD Shield Spear',
'Trash Bow',
'Repair Shield',
'Upgrade Helmet-V']);
// SWORD Spear Shield
