//  Not included in final score
function gladiatorInventory(input) {
    // Mask
    let inventory = input.shift().split(' ');

    function buy(equipment) {
        // should add the equipment at last position in the inventory, but only if it isn't bought already
        // But ig the equipment has upgrade ... might be a problem.
        if (!(inventory.includes(equipment))) {
            inventory.push(equipment);
        }
    }

    function trash(equipment) {
        // delete the equipment if it exists.
        if (inventory.includes(equipment)) {
            inventory.splice(inventory.indexOf(equipment), 1);
        }
    }

    function repair(equipment) {
        // repair the equipment if it exists and place it on last position.
        if (inventory.includes(equipment)) {
            inventory.splice(inventory.indexOf(equipment), 1);
            inventory.push(equipment);
        }
    }

    function upgrade(equipment, upgrade) {
        // check if the equipment exists and insert after it the upgrade in the following format: "{equipment}:{upgrade}"
        if (inventory.includes(equipment)) {
            inventory.splice(inventory.indexOf(equipment) + 1, 0, `${equipment}:${upgrade}`);
        }
    }
    while (input.length > 0) {
        let [command, equipment] = input.shift().split(' ');
        command === 'Buy' ? buy(equipment) : 'pass';
        command === 'Trash' ? trash(equipment) : 'pass';
        command === 'Repair' ? repair(equipment) : 'pass';
        command === 'Upgrade' ? upgrade(equipment.split('-')[0], equipment.split('-')[1]) : 'pass';
    }

    console.log(...inventory);
}

gladiatorInventory(['SWORD Shield Spear', 'Buy Bag', 'Trash Shield', 'Repair Spear', 'Upgrade SWORD-Steel']);
// Should return:

gladiatorInventory(['SWORD Shield Spear', 'Trash Bow', 'Repair Shield', 'Upgrade Helmet-V']);
// Should return: SWORD SWORD:Steel Bag Spear SWORD Spear Shield
