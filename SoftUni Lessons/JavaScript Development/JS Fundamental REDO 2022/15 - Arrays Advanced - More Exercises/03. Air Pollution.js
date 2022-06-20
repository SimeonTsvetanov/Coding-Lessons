function airPollution (map, commands) {
    // MasK - Extremely misleading description of the task...
    // You can't understand if gale is breeze!

    map = map.map(row => row.split(' ').map(Number));

    let gale = (col) => {
        // index is the row where all column’s value drops by 15 PM
        let pm = 20;

        for (let row = 0; row < 5; row ++) {
            map[row][col] - pm >= 0 ? map[row][col] -= pm : map[row][col] = 0;
        }
    };

    let breeze = (row) => {
        // index is the column in all rows where value drops by 20 PM
        let pm = 15;
        for (let col = 0; col < 5; col ++) {
            map[row][col] - pm >= 0 ? map[row][col] -= pm : map[row][col] = 0;
        }
    };

    let smog = (power) => {
        // all blocks in the map increase equally by the given value’s PM
        map.forEach((row, rowIndex) => {
            row.forEach((col, colIndex) => {
                map[rowIndex][colIndex] += power;
            });
        });
    };

    let pollutedAreas = () => {
        let polluted = [];

        for (let row = 0; row < 5; row++) {
            for (let col = 0; col < 5; col++) {
                map[row][col] >= 50 ? polluted.push(`[${row}-${col}]`) : 'pass';
            }
        }

        return polluted;
    }

    commands.forEach(command => {
        const action = command.split(' ')[0];
        const indexOrPower = Number(command.split(' ')[1]);

        if (action === 'breeze') { breeze(indexOrPower); }
        else if (action === 'gale') { gale(indexOrPower); }
        else if (action === 'smog') { smog(indexOrPower); }
    });

    let polluted = pollutedAreas();

    polluted.length > 0 ? console.log(`Polluted areas: ${polluted.join(', ')}`) : console.log(`No polluted areas`);
}

airPollution(['5 7 72 14 4',
        '41 35 37 27 33',
        '23 16 27 42 12',
        '2 20 28 39 14',
        '16 34 31 10 24'],
    ['breeze 1', 'gale 2', 'smog 25']
);

// Polluted areas: [0-2], [1-0], [2-3], [3-3], [4-1]

console.log('----------------------------');

airPollution(['5 7 3 28 32',
            '41 12 49 30 33',
            '3 16 20 42 12',
            '2 20 10 39 14',
            '7 34 4 27 24'],
    ['smog 11', 'gale 3', 'breeze 1', 'smog 2']
);

// No polluted areas