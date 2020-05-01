function shoppingList(input) {
    // Mask
    let groceries = input.shift().split('!');

    while ('command !== Go Shopping!') {
        let [command, item, newItem] = input.shift().split(' ');
        if (command === 'Go') {
            console.log(groceries.join(', '));
            break;
        } else if (command === 'Urgent') {
            // Add the item at the start of the list.  If the item already exists, skip this command.
            if (!groceries.includes(item)) {
                groceries.unshift(item);
            }
        } else if (command === 'Unnecessary') {
            // Remove the item with the given name, only if it exists in the list.
            if (groceries.includes(item)) {
                groceries.splice(groceries.indexOf(item), 1);
            }
        } else if (command === 'Correct') {
            // If the item with the given old name exists, change its name with the new one.
            if (groceries.includes(item)) {
                groceries[groceries.indexOf(item)] = newItem;
            }
        } else if (command === 'Rearrange') {
            // If the grocery exists in the list, remove it from its current position and add it at the end of the list.
            if (groceries.includes(item)) {
                groceries.splice(groceries.indexOf(item), 1);
                groceries.push(item);
            }
        }
    }
}

shoppingList([
    'Tomatoes!Potatoes!Bread',
    'Unnecessary Milk',
    'Urgent Tomatoes',
    'Go Shopping!'
]);
// Should return:
// Tomatoes, Potatoes, Bread

shoppingList([
        'Milk!Pepper!Salt!Water!Banana',
        'Urgent Salt',
        'Unnecessary Grapes ',
        'Correct Pepper Onion',
        'Rearrange Grapes',
        'Correct Tomatoes Potatoes',
        'Go Shopping!'
    ]);
// Should return:
// Milk, Onion, Salt, Water, Banana
