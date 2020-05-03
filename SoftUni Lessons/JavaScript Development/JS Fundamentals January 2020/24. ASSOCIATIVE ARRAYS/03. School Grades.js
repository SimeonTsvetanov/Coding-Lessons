function schoolGrades(input) {
    // Mask
    let students = new Map();

    for (let data of input) {
        data = data.split(' ');
        let student = data.shift();
        let grades = data.map(Number);

        if (students.has(student)) {
            students.set(student, students.get(student).concat(grades));
        } else {
            students.set(student, grades);
        }
    }

    let sorted = Array.from(students.entries()).sort((a, b) => {
       let averageA = (a[1].reduce((a, b) => a + b, 0)) / a[1].length;
       let averageB = (b[1].reduce((a, b) => a + b, 0)) / b[1].length;
       return averageA - averageB;
    });

    for (let [name, grades] of sorted) {
        console.log(`${name}: ${grades.join(', ')}`);
    }
}

schoolGrades(['Lilly 4 6 6 5', 'Tim 5 6', 'Tammy 2 4 3', 'Tim 6 6']);
// Should return:
// Tammy: 2, 4, 3
// Lilly: 4, 6, 6, 5
// Tim: 5, 6, 6, 6
