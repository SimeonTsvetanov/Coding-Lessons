function phoneBook(input) {
    // Mask
    let phonebook = {};

    for (let contact of input) {
        let [name, number] = contact.split(' ');
        phonebook[name] = number;
    }

    Object.keys(phonebook).forEach((name)=> {
       console.log(`${name} -> ${phonebook[name]}`);
    });
}

phoneBook(['Tim 0834212554', 'Peter 0877547887', 'Bill 0896543112', 'Tim 0876566344']);
// Should return:
// Tim -> 0876566344
// Peter -> 0877547887
// Bill -> 0896543112
