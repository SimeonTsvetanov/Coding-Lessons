function mask (params) {
    // MASK
    let grades = [];  // {'grade': 1, 'students': [a,b,c], 'scores': [1, 2, 3]}
    params.forEach(data => {
        data = data.split(' ');
        let student = data[2].split(',')[0];
        let nextGrade = Number(data[4].split(',')[0]) + 1;
        let score = Number(data[10]);

        if (score >= 3) {
            let presentGrade = grades.find(x => x.grade === nextGrade);
            if (presentGrade) {
                presentGrade.students.push(student);
                presentGrade.scores.push(score)
            } else {
                grades.push({'grade': nextGrade, 'students': [student], 'scores': [score]});
            }
        }
    });

    grades.sort((a, b) => a.grade - b.grade);
    grades.forEach(grade => {
        console.log(`${grade.grade} Grade`);
        console.log(`List of students: ${grade.students.join(', ')}`);
        let averageScore = grade.scores.reduce((a, b) => a + b, 0) / grade.scores.length;
        console.log(`Average annual score from last year: ${averageScore.toFixed(2)}`);
        console.log('');
    });
}

mask([
'Student name: George, Grade: 5, Graduated with an average score: 2.75',
'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
'Student name: John, Grade: 9, Graduated with an average score: 2.90',
'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15']);
// 2 Grade
// List of students: Darsy
// Average annual score from last
// year: 5.15
// 3 Grade
// List of students: Steven
// Average annual score from last
// year: 4.90
// 6 Grade
// List of students: Boby
// Average annual score from last
// year: 4.20
// 10 Grade
// List of students: Alex
// Average annual score from last
// year: 3.66
