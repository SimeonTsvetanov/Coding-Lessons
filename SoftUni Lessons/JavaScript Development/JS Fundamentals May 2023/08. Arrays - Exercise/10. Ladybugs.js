function mask (params) {
    // MASK
    let size = params.shift();
    let field= new Array(size).fill(0);
    let bugs = params.shift().split(' ').map(Number);

    // put the bugs on:
    bugs.forEach(bug => {
        if (bug >= 0 && bug < field.length) {
            field[bug] = 1;
        }
    });

    // Create the deltaDirections
    let direction_delta = {
        'right': 1,
        'left': -1
    };

    params.forEach(param => {
        let bug = Number(param.split(' ')[0]);          // Get the current bug index on the field
        let direction = direction_delta[param.split(' ')[1]];   // make the direction positive or negative
        let distance = Number(param.split(' ')[2]);     // get the jump distance to fly over

        // First check if bug exists:
        if (bug >= 0 && bug < field.length && field[bug] == 1) {
            // Now lets move its fat ass:

            field[bug] = 0;              // Remove the bug from the field
            let flying = true;  // Make a stop for the while loop!

            let current_bug = bug;  // Create a variable to keep the next position

            while (flying) {
                let next_spot = (current_bug) + distance * direction;  // Get the next position:

                // First check if it can land:
                if (next_spot >= 0 && next_spot < field.length && field[next_spot] === 0) {
                    field[next_spot] = 1;  // Put the bug on the map again.
                    flying = false;        // Stop the loop!
                }
                // Next check if it will fly away:
                else if (next_spot < 0 || next_spot >= field.length) {
                    flying = false;  // Stop the loop!
                }
                // Finally check if the position in taken:
                else if (next_spot >= 0 && next_spot < field.length && field[next_spot] === 1) {
                    current_bug = next_spot;  // Change the temporary location, and continue the loop!
                }
            }
        }
    });

    console.log(...field);
}

mask([ 3, '0 1',
'0 right 1',
'2 right 1' ]);
// 0 1 0

console.log('-------------------------');

mask([ 3, '0 1 2',
'0 right 1',
'1 right 1',
'2 right 1']);
// 0 0 0
