function inventory(input) {
    // Mask
    let items = input.shift().split(', ');

    while ('command != "Craft!"') {
        let [command, item] = input.shift().split(' - ');
        if (command === 'Craft!') {
            console.log(items.join(', '));
            break;
        } else if (command === 'Collect') {
            // Add the given item in your inventory. If the item already exists
            if (!items.includes(item)) {
                items.push(item);
            }
        } else if (command === 'Drop') {
            // Remove the item from your inventory, if it exists
            if (items.includes(item)) {
                items.splice(items.indexOf(item), 1);
            }
        } else if (command === 'Combine Items') {
            // Check if the old item exists, if so, add the new item after the old one.
            let [oldItem, newItem] = item.split(':');
            if (items.includes(oldItem)) {
                items.splice(items.indexOf(oldItem) + 1, 0, newItem);
            }
        } else if (command === 'Renew') {
            // If the given item exists, you should change its position and put it last in your inventory.
            if (items.includes(item)) {
                items.splice(items.indexOf(item), 1);
                items.push(item);
            }
        }
    }
}

inventory([ 'Iron, Wood, Sword', 'Collect - Gold', 'Drop - Wood', 'Craft!' ]);
// Should return:
// Iron, Sword, Gold

inventory([
    'Iron, Sword',
    'Drop - Bronze',
    'Combine Items - Sword:Bow',
    'Renew - Iron',
    'Craft!'
]);
// Should return:
// Sword, Bow, Iron