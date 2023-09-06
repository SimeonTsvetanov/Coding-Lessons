function mask (params) {
    // MASK
    let companies = {};  // { 'companyName': ['id1', 'id2', 'id3'], ... }

    params.forEach(param => {
        let [company, ids] = param.split(' -> ');

        if (!(company in companies)) { companies[company] = []; }
        if (!(companies[company].includes(ids))) { companies[company].push(ids); }
    });

    let sorted = Object.keys(companies).sort((a, b) => {return a.localeCompare(b)});
    sorted.forEach(c => {
        console.log(c);
        companies[c].forEach(e => { console.log(`-- ${e}`); });
    });
}

mask([
'SoftUni -> AA12345',
'SoftUni -> BB12345',
'Microsoft -> CC12345',
'HP -> BB12345'
]);
// HP
// -- BB12345
// Microsoft
// -- CC12345
// SoftUni
// -- AA12345
// -- BB12345

console.log('-------------------------------------');

mask([
'SoftUni -> AA12345',
'SoftUni -> CC12344',
'Lenovo -> XX23456',
'SoftUni -> AA12345',
'Movement -> DD11111'
]);
// Lenovo
// -- XX23456
// Movement
// -- DD11111
// SoftUni
// -- AA12345
// -- CC12344
