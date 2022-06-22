function addressBook (data) {
    // MasK

    let book = {};

    data.forEach(entry => {
        let [name, address] = entry.split(":");
        book[name] = address;
    });

    let sortedKeys = Object.keys(book).sort((a, b) => a.localeCompare(b));
    sortedKeys.forEach(name => {
        console.log(`${name} -> ${book[name]}`);
    });
}


addressBook(['Tim:Doe Crossing',
    'Bill:Nelson Place',
    'Peter:Carlyle Ave',
    'Bill:Ornery Rd']
);

// Bill -> Ornery Rd
// Peter -> Carlyle Ave
// Tim -> Doe Crossing
