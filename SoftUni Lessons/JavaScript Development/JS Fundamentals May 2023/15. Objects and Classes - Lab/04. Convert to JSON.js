function mask (name, lastName, hairColor) {
    // MASK
    const object = {'name': name, 'lastName': lastName, 'hairColor': hairColor};
    console.log(JSON.stringify(object));
}

mask('George', 'Jones',
'Brown');
// {"name":"George","lastName":"Jones","hairColor":"Brown"}

console.log('-------------------------------------');

mask('Peter', 'Smith',
'Blond'
);
// {"name":"Peter","lastName":"Smith","hairColor":"Blond"}

