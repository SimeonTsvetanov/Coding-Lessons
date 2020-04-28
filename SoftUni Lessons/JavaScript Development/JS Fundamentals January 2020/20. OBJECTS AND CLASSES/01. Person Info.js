function personInfo(fName, lName, age) {
    // Mask
    person = {
        firstName: fName,
        lastName: lName,
        age: age,
    };

    for (let key in person) {
        console.log(`${key}: ${person[key]}`);
    }
}

personInfo('Peter','Pan','20');  // Should return:
// firstName: Peter
// lastName: Pan
// age: 20

personInfo('Simeon','Tsvetanov','30');  // Should return:
// firstName: Simeon
// lastName: Tsvetanov
// age: 30
