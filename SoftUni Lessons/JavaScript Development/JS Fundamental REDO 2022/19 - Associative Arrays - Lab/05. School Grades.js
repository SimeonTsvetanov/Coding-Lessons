function schoolGrades (data) {
    // MasK
    function sortObject(obj) {
        let sortedKVP = Array.from(Object.entries(obj)).sort((a, b) => {
            // Example Sort buy value (NUMBER) the smallest FIRST
            return a[0].localeCompare(b[0]) || 'if you want a second condition';
        });
        let sortedObject = {}
        for (let i = 0; i < sortedKVP.length; i++) {
            sortedObject[sortedKVP[i][0]] = sortedKVP[i][1]
        }
        return sortedObject;
    }

    function find_average_num_array(array) {
        // return the average number from array of numbers, if the array is empty return 0
        return array.length > 0 ? array.reduce((a, b) => a + b, 0) / array.length : 0;
    }

    let students = {} // {student1: [grade1, grade2..], student2: [...], ...}

    data.forEach(data => {
        data = data.split(' ');
        let name = data.shift();
        let grades = data.map(Number);

        students.hasOwnProperty(name) ? students[name] = students[name].concat(grades) : students[name] = grades;
    });

    let sortedStudents = sortObject(students);

    for (const [student, grades] of Object.entries(sortedStudents)) {
        let average = find_average_num_array(grades).toFixed(2);
        console.log(`${student}: ${average}`);
    }
}

schoolGrades(['Lilly 4 6 6 5',
    'Tim 5 6',
    'Tammy 2 4 3',
    'Tim 6 6']
);

// Lilly: 5.25
// Tammy: 3.00
// Tim: 5.75
