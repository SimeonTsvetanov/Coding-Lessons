function train(input) {
    // Mask
    let wagons = input.shift().split(' ').map(Number);
    let maxCapacity = Number(input.shift());

    for (let command of input) {
        command = command.split(' ');
        if (command[0] === 'Add') {
            // We add new cart...
            wagons.push(Number(command[1]));
        } else {
            // We will need to find a place for the new passengers...
            let needed = Number(command[0]);
            for (let index = 0; index < wagons.length; index += 1){
                let taken = wagons[index];
                if (needed + taken <= maxCapacity) {
                    // Space in enough.
                    wagons[index] += needed;
                    break;  // Break the loop.
                }
            }
        }
    }

    console.log(...wagons);
}

train(['32 54 21 12 4 0 23',
    '75',
    'Add 10',
    'Add 0',
    '30',
    '10',
    '75']
);
// Should return: 72 54 21 12 4 75 23 10 0

train(['0 0 0 10 2 4',
    '10',
    'Add 10',
    '10',
    '10',
    '10',
    '8',
    '6']);
// Should return: 10 10 10 10 10 10 10
