function phoneBook (data) {
    // MasK
    let phonebook = {};

    data.forEach(nameAndPhoneNumber => {
        let [name, number] = nameAndPhoneNumber.split(" ");
        phonebook[name] = number;
    });

    for (const [name, number] of Object.entries(phonebook)) {
        console.log(`${name} -> ${number}`);
    }
}

phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
);

// Tim -> 0876566344
// Peter -> 0877547887
// Bill -> 0896543112
