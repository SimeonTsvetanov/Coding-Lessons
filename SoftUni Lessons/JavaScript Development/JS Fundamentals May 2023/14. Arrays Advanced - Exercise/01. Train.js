function mask (params) {
    // MASK
    // You will be given an array of strings.

    // The first element will be a string containing wagons (numbers).
    let wagons = params.shift().split(' ').map(Number);
    // Each number inside the string represents the number of passengers that are currently in a wagon.

    // The second element in the array will be the max capacity of each wagon (single number).
    let max_capacity = Number(params.shift());

    // The rest of the elements will be commands in the following format:
    params.forEach(command => {
        // Add {passengers} – add a wagon to the end with the given number of passengers.
        if (command.split(' ')[0] === 'Add') {
            wagons.push(Number(command.split(' ')[1]));
        }

        //{passengers} - find an existing wagon to fit all the passengers (starting from the first wagon)
        else {
            let hitchhikers = Number(command);

            for (const [index, passengers] of wagons.entries()) {
                if (passengers + hitchhikers <= max_capacity) {
                    // We can fit them asses:
                    wagons[index] += hitchhikers;
                    break;
                }
            }
        }
    });

    // At the end, print the final state of the train (all the wagons separated by a space):
    console.log(wagons.join(' '));
}

mask(['0 0 0 10 2 4',
'10',
'Add 10',
'10',
'10',
'10',
'8',
'6']);
// 10 10 10 10 10 10 10

console.log('-------------------------------------');


mask(['32 54 21 12 4 0 23',
'75',
'Add 10',
'Add 0',
'30',
'10',
'75']);
// 72 54 21 12 4 75 23 10 0
