function companyUsers (data) {
    // MasK
    function sortObject(obj) {
        let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
            // Example Sort buy value (NUMBER) the smallest FIRST
            return a[0].localeCompare(b[0]) || 'if you want a second condition';
        });
        let sortedObject = {}
        for (let i = 0; i < sortedKVP.length; i ++) {
            sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
        }
        return sortedObject;
    }

    let companies = {};

    data.forEach(entry => {
        let [companyName, employeeID] = entry.split(' -> ');
        companies.hasOwnProperty(companyName) ? companies[companyName].push(employeeID) : companies[companyName] = [employeeID];
    });

    let sortedCompanies = sortObject(companies);

    for (let [name, ids] of Object.entries(sortedCompanies)) {
        ids = [...new Set(ids)];
        console.log(name);
        ids.forEach(id => {
            console.log(`-- ${id}`);
        });
    }
}

companyUsers([
        'SoftUni -> AA12345',
        'SoftUni -> BB12345',
        'Microsoft -> CC12345',
        'HP -> BB12345'
    ]
);

// HP
// -- BB12345
// Microsoft
// -- CC12345
// SoftUni
// -- AA12345
// -- BB12345

console.log();

companyUsers([
        'SoftUni -> AA12345',
        'SoftUni -> CC12344',
        'Lenovo -> XX23456',
        'SoftUni -> AA12345',
        'Movement -> DD11111'
    ]
);

// Lenovo
// -- XX23456
// Movement
// -- DD11111
// SoftUni
// -- AA12345
// -- CC12344
