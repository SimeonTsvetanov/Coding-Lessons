function weaponsmith(input) {
    // Mask
    let weapon = input.shift().split('|');

    function moveLeft(index) {
        if (index > 0 && index < weapon.length) {
            let element = weapon[index];
            weapon.splice(index, 1);
            weapon.splice(index - 1, 0, element);
        }
    }

    function moveRight(index) {
        if (index >= 0 && index < weapon.length - 1) {
            let element = weapon[index];
            weapon.splice(index, 1);
            weapon.splice(index + 1, 0, element);
        }
    }

    function checkEven() {
        let even = weapon.filter((element, index) => index % 2 === 0);
        console.log(even.join(' '));
    }

    function checkOdd() {
        let odd = weapon.filter((element, index) => index % 2 === 1);
        console.log(odd.join(' '));
    }

    while ('The Earth Spins') {
        let command = input.shift().split(' ');
        if (command[0] === 'Done') { break; }
        command[0] === 'Move' && command[1] === 'Left' ? moveLeft(Number(command[2])) : 'gas';
        command[0] === 'Move' && command[1] === 'Right' ? moveRight(Number(command[2])) : 'pass';
        command[0] === 'Check' && command[1] === 'Even' ? checkEven() : 'or';
        command[0] === 'Check' && command[1] === 'Odd' ? checkOdd() : 'ass';
    }

    console.log(`You crafted ${weapon.join('')}!`);
}

weaponsmith([
    'ha|Do|mm|om|er',
    'Move Right 0',
    'Move Left 3',
    'Check Odd',
    'Move Left 2',
    'Move Left 10',
    'Move Left 0',
    'Done'
]);
// Should return:
// ha mm
// You crafted Doomhammer!


weaponsmith([
    'ri|As|er|hb|ng',
    'Move Left 1',
    'Move Right 2',
    'Move Right 3',
    'Move Left 2',
    'Done'
]);
// Should return:
// You crafted Ashbringer!
