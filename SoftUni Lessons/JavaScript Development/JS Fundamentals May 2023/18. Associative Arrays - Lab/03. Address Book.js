function mask (params) {
    // MASK
    let names = {}

    params.forEach(param=> {
        let name = param.split(':')[0];
        let address = param.split(':')[1];
        names[name] = address;
    });

    for (let [name, address] of Object.entries(names).sort((a, b) => a[0].localeCompare(b[0]))) {
        console.log(`${name} -> ${address}`);
    }
}

mask(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd']);
// Bill -> Ornery Rd
// Peter -> Carlyle Ave
// Tim -> Doe Crossing

console.log('-------------------------------------');

mask(['Bob:Huxley Rd',
'John:Milwaukee Crossing',
'Peter:Fordem Ave',
'Bob:Redwing Ave',
'George:Mesta Crossing',
'Ted:Gateway Way',
'Bill:Gateway Way',
'John:Grover Rd',
'Peter:Huxley Rd',
'Jeff:Gateway Way',
'Jeff:Huxley Rd']);
// Bill -> Gateway Way
// Bob -> Redwing Ave
// George -> Mesta
// Crossing
// Jeff -> Huxley Rd
// John -> Grover Rd
// Peter -> Huxley Rd
// Ted -> Gateway Way
