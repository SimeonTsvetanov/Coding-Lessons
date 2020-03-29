function examPreparation(data) {
    let limitBadScores = Number(data.shift());
    let badScores = 0;

    let totalScore = 0;
    let countSubjects = 0;
    let lastTask = undefined;

    while ("Lector says Enough or TOO many bad scores") {
        let subject = data.shift();
        if (subject === 'Enough') {
            console.log(`Average score: ${(totalScore / countSubjects).toFixed(2)}`);
            console.log(`Number of problems: ${countSubjects}`);
            console.log(`Last problem: ${lastTask}`);
            break;
        }
        let score = Number(data.shift());
        if (score <= 4) {
            badScores += 1;
            if (badScores === limitBadScores) {
                console.log(`You need a break, ${badScores} poor grades.`);
                break;
            }
        }
        totalScore += score;
        countSubjects += 1;
        lastTask = subject;
    }    
}

examPreparation([3, 'Money', 6, 'Story', 4, 'Spring Time', 5, 'Bus', 6, 'Enough']);
// Expected Output:
// Average score: 5.25
// Number of problems: 4
// Last problem: Bus

examPreparation([2, 'Income', 3, 'Game Info', 6, 'Best Player', 4]);
// Expected Output:
// You need a break, 2 poor grades.