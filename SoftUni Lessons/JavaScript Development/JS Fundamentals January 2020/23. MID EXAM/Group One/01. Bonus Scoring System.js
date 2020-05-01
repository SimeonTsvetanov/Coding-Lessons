function bonusScoringSystem(input = []) {
    // Mask
    let students = Number(input.shift());
    let lectures = Number(input.shift());
    let additionalBonus = Number(input.shift());

    let maxBonus = 0;  // IT HAS TO BE ***ZERO*** Judge- related Reasons.
    let maxLectures = 0;

    for (let student = 1; student <= students; student++) {
        let attendances = Number(input.shift());
        let bonus = attendances / lectures * (5 + additionalBonus);
        if (bonus > maxBonus) {
            maxBonus = bonus;
            maxLectures = attendances;
        }
    }

    console.log(`Max Bonus: ${Math.round(maxBonus)}.`);
    console.log(`The student has attended ${maxLectures} lectures.`);
}

bonusScoringSystem(['5',  '25', '30', '12', '19', '24', '16', '20']);
// Should return:
// Max Bonus: 34.
// The student has attended 24 lectures.


bonusScoringSystem(['10', '30', '14', '8', '23', '27', '28', '15', '17', '25', '26', '5', '18']);
// Should return:
// Max Bonus: 18.
// The student has attended 28 lectures.