function gladiatorInventory (data) {
    // MasK
    let inventory = data.shift().split(' ');

    let removeAt = (array, index) => {
        return array.splice(index, 1);
    }

    let insertAt = (array, index, element) => {
        Array.isArray(element) ? array.splice(index, 0, ...element) : array.splice(index, 0, element);
    }

    data.forEach(command => {
        let [action, weapon] = command.split(' ');

        if (action === "Buy") {
            !inventory.includes(weapon) ? inventory.push(weapon) : 'pass';
        } else if (action === 'Trash') {
            inventory.includes(weapon) ? removeAt(inventory, inventory.indexOf(weapon)) : 'pass';
        } else if (action === 'Repair') {
            if (inventory.includes(weapon)) {
                removeAt(inventory, inventory.indexOf(weapon));
                inventory.push(weapon);
            }
        } else if (action === 'Upgrade') {
            let [weaponToUpgrade, upgrade] = weapon.split('-');
            if (inventory.includes(weaponToUpgrade)) {
                insertAt(inventory, inventory.indexOf(weaponToUpgrade) + 1, `${weaponToUpgrade}:${upgrade}`);
            }
        }
    });

    console.log(...inventory);
}

gladiatorInventory(['SWORD Shield Spear',
    'Buy Bag',
    'Trash Shield',
    'Repair Spear',
    'Upgrade SWORD-Steel']
);

// SWORD SWORD:Steel Bag Spear