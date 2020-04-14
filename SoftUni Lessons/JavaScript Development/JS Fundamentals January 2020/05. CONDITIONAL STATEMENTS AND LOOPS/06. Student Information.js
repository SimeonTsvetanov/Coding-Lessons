function studentInformation(name, age, grade) {
    // Mask
    console.log(`Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`);
}

studentInformation('John', 15, 5.54678);  // Should return:
// Name: John, Age: 15, Grade: 5.55

studentInformation('Steve', 16, 2.1426);  // Should return:
// Name: Steve, Age: 16, Grade: 2.14
