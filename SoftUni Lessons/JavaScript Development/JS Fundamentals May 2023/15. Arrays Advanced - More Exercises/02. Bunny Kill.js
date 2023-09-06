function mask (input) {
    // MASK

    // Get and sort the input:

    let bombs = input.pop().split(' ').map(x => x.split(',').map(Number));
    let hangar = input.map(x => x.split(' ').map(Number));

    // Set the result variables:

    let damage = 0;
    let confirmedKills = 0;

    // Function to check if given coordinates are in given matrix.
    const coordExistsInMatrix = ([r, c], m) => { return r >=0 && r < m.length && c >= 0 && c < m[r].length }

    // Delta moves (for cleaner code!)
    const moves = {
        'upperLeft': [-1, -1],
        'up': [-1, 0],
        'upperRight': [-1, 1],
        'left': [0, -1],
        'right': [0, +1],
        'bottomLeft': [+1, -1],
        'down': [+1, 0],
        'bottomRight': [+1, +1]
    };

    // Now let's Explode the bombs:

    for (const bomb of bombs) {
        if (!coordExistsInMatrix(bomb, hangar)) { continue }  // Just make sure bomb Exists!
        if (hangar[bomb[0]][bomb[1]] <= 0) {continue}          // And it has not exploded yet.

        const bombValue = hangar[bomb[0]][bomb[1]];           // Get the bomb value
        hangar[bomb[0]][bomb[1]] = 0;                         // Remove the bomb from the hangar
        damage += bombValue;                                  // Add the value to the total damage
        confirmedKills += 1;                                  // It's been neutralised

        // Taking casualties with it:

        for (let [move, [r, c]] of Object.entries(moves)) {
            let casualtiesCoords = [bomb[0] + r, bomb[1] + c];                  // Get the coords of the casualty
            if (!coordExistsInMatrix(casualtiesCoords, hangar)) { continue }           // Make sure the casualty Exists!
            const casualtyValue = hangar[casualtiesCoords[0]][casualtiesCoords[1]];    // Get the casualty Value

            // Take the damage:
            hangar[casualtiesCoords[0]][casualtiesCoords[1]] = Math.max((casualtyValue - bombValue), 0);
        }
    }

    // And finally let's make a killing spree !?!

    hangar.forEach((row) => {
        row.forEach(enemyValue => {
           if (enemyValue > 0) {
               damage += enemyValue;   // Add the damage value
               confirmedKills += 1;    // Add the kill
           }
        });
    });

    // Now present your happiness:

    console.log(damage);
    console.log(confirmedKills);
}

mask(['5 10 15 20',
'10 10 10 10',
'10 15 10 10',
'10 10 10 10',
'2,2 0,1']);
// 70
// 7

console.log('-------------------------------------');

mask(['10 10 10',
'10 10 10',
'10 10 10',
'0,0']);
// 60
// 6
