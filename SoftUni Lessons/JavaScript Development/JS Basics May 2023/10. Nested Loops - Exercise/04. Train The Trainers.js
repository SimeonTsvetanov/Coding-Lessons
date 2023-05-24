function solution(params) {
    // MasK
    let trainersCount = Number(params.shift());
    let subjects = {};  // Subject : [Scores]
    let allScores = [];
    while ('Finish') {
        let subject = params.shift();
        if (subject === 'Finish') { break; }
        for (let trainerScore = 0; trainerScore < trainersCount; trainerScore++) {
            if (!subjects[subject]) { subjects[subject] = []; }
            currentScore = Number(params.shift());
            subjects[subject].push(currentScore);
            allScores.push(Number(currentScore));
        }
    }

    Object.entries(subjects).forEach(([subject, scores]) => {
        console.log(`${subject} - ${(scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(2)}.`);
    });
    console.log(`Student's final assessment is ${(allScores.reduce((a, b) => a + b, 0) / allScores.length).toFixed(2)}.`);
}

solution(["2",
"While-Loop",
"6.00",
"5.50",
"For-Loop",
"5.84",
"5.66",
"Finish"]);

// While-Loop - 5.75.
// For-Loop - 5.75.
// Student's final assessment is 5.75.

console.log('********************************');

solution(["3",
"Arrays",
"4.53",
"5.23",
"5.00",
"Lists",
"5.83",
"6.00",
"5.42",
"Finish"]);

// Arrays - 4.92.
// Lists - 5.75.
// Student's final assessment is 5.34.
