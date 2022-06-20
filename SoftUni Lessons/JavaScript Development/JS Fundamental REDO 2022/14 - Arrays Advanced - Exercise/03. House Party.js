function houseParty (commands) {
    // MasK
    let guests = [];

    commands.forEach(command => {
        command = command.split(' ');
        const name = command[0];
        if (command.length === 3) {
            guests.includes(name) ? console.log(`${name} is already in the list!`) : guests.push(name);
        } else {
            guests.includes(name) ? guests.splice(guests.indexOf(name), 1) : console.log(`${name} is not in the list!`);
        }
    });

    console.log(guests.join(`\n`));
}

houseParty(['Allie is going!',
    'George is going!',
    'John is not going!',
    'George is not going!']
);

// John is not in the list!
// Allie

houseParty(['Tom is going!',
    'Annie is going!',
    'Tom is going!',
    'Garry is going!',
    'Jerry is going!']
);

// Tom is already in the list!
// Tom
// Annie
// Garry
// Jerry
