function mask (...params) {
    // MASK
    let sofia = params.shift().map(x => x.split(' ').map(Number));
    let forces = params.shift();

    let weather = {
        'breeze': (indexRow) => {
            for (let col = 0; col < 5; col++) {
                sofia[indexRow][col] = Math.max(sofia[indexRow][col] - 15, 0);
            }},
        'gale': (indexCol) => {
            for (let row = 0; row < 5; row++) {
                sofia[row][indexCol] = Math.max(sofia[row][indexCol] - 20, 0);
            }},
        'smog': (value) => {
            for (let row = 0; row < 5; row++) {
                for (let col = 0; col < 5; col++) { sofia[row][col] += value; }
            }},
    };

    forces.forEach(data => {
        let force = data.split(' ')[0];
        let indexOrValue = Number(data.split(' ')[1]);

        weather[force](indexOrValue);
    });

    const pollutedAreas = []
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            (sofia[row][col] >= 50) ? pollutedAreas.push(`[${row}-${col}]`) : 'pass';
        }
    }

    (pollutedAreas.length > 0)
        ? console.log(`Polluted areas: ${pollutedAreas.join(', ')}`)
        : console.log('No polluted areas');
}

mask(['5 7 72 14 4',
'41 35 37 27 33',
'23 16 27 42 12',
'2 20 28 39 14',
'16 34 31 10 24'],
['breeze 1', 'gale 2', 'smog 25']);
// Polluted areas: [0-2], [1-0], [2-3], [3-3], [4-1]

console.log('-------------------------------------');

mask(['5 7 3 28 32',
'41 12 49 30 33',
'3 16 20 42 12',
'2 20 10 39 14',
'7 34 4 27 24'],
['smog 11', 'gale 3', 'breeze 1',
'smog 2']);
// No polluted areas
