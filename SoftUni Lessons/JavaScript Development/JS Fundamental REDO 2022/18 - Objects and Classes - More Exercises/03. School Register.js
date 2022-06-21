function schoolRegister (data) {
    // MasK

    class Grade {
        constructor(grade) {
            this.grade = grade;
            this.students = [];
            this.scores = [];
        }

        get averageScore() {
            let sumScores = this.scores.reduce((a, b) => a + b, 0);
            let lengthScore = this.scores.length;
            let average = sumScores / lengthScore;
            return average.toFixed(2);
        }
    }

    let grades = [];  // To keep all the grades

    // Now let's extract and sort the data:
    data.forEach(dataEntry => {
        let [nameData, gradeData, scoreData] = dataEntry.split(", ");

        let currentStudent = nameData.split(': ')[1];
        let currentGrade = Number(gradeData.split(': ')[1]) + 1;
        let currentScore = Number(scoreData.split(': ')[1]);

        // Check if the Score is higher than the limit 3.00
        if (currentScore >= 3) {
            // Let's check if we have the grade saved already:
            let presentGrade = grades.find(x => {
                return x.grade === currentGrade
            });
            if (presentGrade) {
                // We have it already:
                presentGrade.students.push(currentStudent);  // Add the new Student
                presentGrade.scores.push(currentScore);      // Add his score
            } else {
                // We don't have it:
                let newGrade = new Grade(currentGrade);  // Create the Grade
                newGrade.students.push(currentStudent);  // Add the student
                newGrade.scores.push(currentScore);      // Add the score
                grades.push(newGrade);                   // And the grade to the array

            }
        }
    });

    // Sort the grades correctly:
    grades.sort((a, b) => a.grade - b.grade);

    // Print the result:
    grades.forEach(grade => {
        console.log(`${grade.grade} Grade`);
        console.log(`List of students: ${grade.students.join(', ')}`);
        console.log(`Average annual score from last year: ${grade.averageScore}`);
        console.log();
    });
}

// schoolRegister([
//         "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
//         "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
//         "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
//         "Student name: George, Grade: 8, Graduated with an average score: 2.83",
//         "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
//         "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
//         "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
//         "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
//         "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
//         "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
//         "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
//         "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
//     ]
// );

// 9 Grade
// List of students: Mark, Daryl
// Average annual score from last year: 5.35
//
// 10 Grade
// List of students: Ethan, Joey, Bill
// Average annual score from last year: 5.52
//
// 11 Grade
// List of students: Steven, Philip, Gavin
// Average annual score from last year: 4.42
//
// 12 Grade
// List of students: Bob, Peter
// Average annual score from last year: 5.02

schoolRegister([
        'Student name: George, Grade: 5, Graduated with an average score: 2.75',
        'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
        'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
        'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
        'Student name: John, Grade: 9, Graduated with an average score: 2.90',
        'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
        'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
    ]
);

// 2 Grade
// List of students: Darsy
// Average annual score from last year: 5.15
//
// 3 Grade
// List of students: Steven
// Average annual score from last year: 4.90
//
// 6 Grade
// List of students: Boby
// Average annual score from last year: 4.20
//
// 10 Grade
// List of students: Alex
// Average annual score from last year: 3.66
