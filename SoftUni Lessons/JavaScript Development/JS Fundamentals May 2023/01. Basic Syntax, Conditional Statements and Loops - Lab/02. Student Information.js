/**
 * @param {string} name
 * @param {number} age
 * @param {number} grade
 */
function mask (name, age, grade) {
    // MASK
    let result = `Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`
    return console.log(result)
}

mask('John', 15, 5.54678);
//  Name: John, Age: 15, Grade: 5.55

mask('Steve', 16, 2.1426);
// Name: Steve, Age: 16, Grade: 2.14
