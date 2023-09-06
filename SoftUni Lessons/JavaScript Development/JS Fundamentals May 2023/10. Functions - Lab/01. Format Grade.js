function format_grade (grade) {
    // MASK - most unclear task description ever. WTF :D:D:D
    if (grade < 3.00) {console.log(`Fail (${2})`)}
    else if (grade >= 3.00 && grade < 3.50) {console.log(`Poor (${grade.toFixed(2)})`)}
    else if (grade >= 3.50 && grade < 4.50) {console.log(`Good (${grade.toFixed(2)})`)}
    else if (grade >= 4.50 && grade < 5.50) {console.log(`Very good (${grade.toFixed(2)})`)}
    else if (grade >= 5.50) {console.log(`Excellent (${grade.toFixed(2)})`)}
}

format_grade(3.33);
// Poor (3.33)

format_grade(4.50);
// Very good (4.50)
