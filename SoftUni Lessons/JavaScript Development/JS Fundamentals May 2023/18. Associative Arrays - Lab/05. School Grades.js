function mask (params) {
    // MASK
    let students = {};

    params.forEach(param => {
        param = param.split(' ');
        let name = param.shift();
        let scores = param.map(Number);
        (name in students) ? students[name] = students[name].concat(scores): students[name]= scores;
    });

    Object.keys(students)
        .sort((a, b) => a.localeCompare(b))
        .forEach(student => {
            let average = students[student].reduce((a, b) => a + b, 0) / students[student].length;
            console.log(`${student}: ${average.toFixed(2)}`);
        });
}

mask(['Lilly 4 6 6 5',
'Tim 5 6',
'Tammy 2 4 3',
'Tim 6 6']);
// Lilly: 5.25
// Tammy: 3.00
// Tim: 5.75

console.log('-------------------------------------');

mask(['Steven 3 5 6 4',
'George 4 6',
'Tammy 2 5 3',
'Steven 6 3']);
// George: 5.00
// Steven: 4.50
// Tammy: 3.33
