function mask (params) {
    // MASK

    let guests = [];

    params.forEach(param => {
        let [name, ...rest] = param.split(' ');
        if (rest.length === 2) {
            (guests.includes(name))
                ? console.log(`${name} is already in the list!`)
                : guests.push(name);
        } else {
            (guests.includes(name))
                ? guests.splice(guests.indexOf(name), 1)
                : console.log(`${name} is not in the list!`);
        }
    });

    console.log(guests.join('\n'));
}

mask(['Allie is going!',
'George is going!',
'John is not going!',
'George is not going!']);
// John is not in the list!
// Allie

console.log('-------------------------------------');

mask(['Tom is going!',
'Annie is going!',
'Tom is going!',
'Garry is going!',
'Jerry is going!']);
// Tom is already in the list!
// Tom
// Annie
// Garry
// Jerry
