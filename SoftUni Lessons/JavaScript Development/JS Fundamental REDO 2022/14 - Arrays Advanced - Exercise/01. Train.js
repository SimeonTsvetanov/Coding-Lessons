function train (data) {
    // MasK
    let wagons = data.shift();
    wagons = wagons.split(' ').map(Number);
    let maxCapacity = +data.shift();

    for (let command of data) {
        command = command.split(' ');
        if (command.length === 2) {
            // add a wagon to the end with the given number of passengers.
            wagons.push(+command[1]);
        } else {
            // find an existing wagon to fit all the passengers (starting from the first wagon)
            const neededSpace = +command[0];
            for (let i = 0; i < wagons.length; i++) {
                let wagon = wagons[i]
                if (wagon + neededSpace <= maxCapacity) {
                    wagons[i] += neededSpace;
                    break;
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

// 72 54 21 12 4 75 23 10 0