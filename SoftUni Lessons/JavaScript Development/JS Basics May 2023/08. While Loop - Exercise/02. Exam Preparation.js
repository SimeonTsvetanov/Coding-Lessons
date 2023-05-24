function solution(params) {
    // MasK
    let maxBadScores = Number(params.shift());
    let badScores = 0;
    let scores = {};

    while ('true') {
        let command = params.shift();
        
        if (command === 'Enough') {
            console.log(`Average score: ${(Object.values(scores).reduce((a, b) => a + b, 0) / Object.keys(scores).length).toFixed(2)}`);
            console.log(`Number of problems: ${Object.keys(scores).length}`);
            console.log(`Last problem: ${Object.keys(scores).pop()}`);
            break;
        }
        
        let subject = command;
        let score = Number(params.shift());
        scores[subject] = score;

        if (score <= 4) {
            badScores ++;
            if (badScores === maxBadScores) {
                console.log(`You need a break, ${badScores} poor grades.`);
                break;
            }
        }   
    }
}

solution(["3",
"Money",
"6",
"Story",
"4",
"Spring Time",
"5",
"Bus",
"6",
"Enough"])

// Average score: 5.25
// Number of problems: 4
// Last problem: Bus


console.log('********************************');

solution(["2",
"Income",
"3",
"Game Info",
"6",
"Best Player",
"4"])

// You need a break, 2 poor grades.
