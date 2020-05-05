function companyUsers(input) {
    // Mask
    let companies = {};

    input.forEach(data => {
        let [company, employeeId] = data.split(` -> `);
        if (companies.hasOwnProperty(company)) {
            if (!companies[company].includes(employeeId)) {
                companies[company].push(employeeId);
            }
        } else {
            companies[company] = [employeeId];
        }
    })

    for (let company of Object.keys(companies).sort()) {
        console.log(company);
        companies[company].forEach(employee => {
            console.log(`-- ${employee}`);
        })
    }
}

companyUsers(['SoftUni -> AA12345', 'SoftUni -> BB12345', 'Microsoft -> CC12345', 'HP -> BB12345']);
// Should return:
// HP
// -- BB12345
// Microsoft
// -- CC12345
// SoftUni
// -- AA12345
// -- BB12345


companyUsers(['SoftUni -> AA12345', 'SoftUni -> CC12344',
    'Lenovo -> XX23456', 'SoftUni -> AA12345', 'Movement -> DD11111']);
// Should return:
// Lenovo
// -- XX23456
// Movement
// -- DD11111
// SoftUni
// -- AA12345
// -- CC12344
