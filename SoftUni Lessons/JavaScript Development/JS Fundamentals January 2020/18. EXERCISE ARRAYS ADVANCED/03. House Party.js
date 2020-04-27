function houseParty(input) {
    // Mask --> Yeah, it looks strange... but i come from Python!

    // Create the array:
    let guests = [];

    function add (name) {
        // Adding new guests
        guests.includes(name)
            ? console.log(`${name} is already in the list!`)
            : guests.push(name);
    }

    function remove(name) {
        // Removing the guest
        guests.includes(name)
            ? guests.splice(guests.indexOf(name), 1)
            : console.log(`${name} is not in the list!`);
    }

    // Main Loop:
    input.map(command => command.split(' ').length === 3
        ? add(command.split(' ')[0])
        : remove(command.split(' ')[0]));

    // Log the result
    console.log(guests.join('\n'));
}

houseParty(['Allie is going!',
    'George is going!',
    'John is not going!',
    'George is not going!']);
// Should return:
// John is not in the list!
// Allie

houseParty(['Tom is going!',
    'Annie is going!',
    'Tom is going!',
    'Garry is going!',
    'Jerry is going!']);
// Should return:
// Tom is already in the list!
// Tom
// Annie
// Garry
// Jerry
