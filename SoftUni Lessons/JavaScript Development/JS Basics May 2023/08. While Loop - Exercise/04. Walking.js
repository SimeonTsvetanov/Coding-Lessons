function solution(params) {
    // MasK
    let steps = 0;

    while (params.length > 0) {
        let command = params.shift();

        if (command === 'Going home') {
            steps += Number(params.shift());
            (steps >= 10000) 
            ? console.log(`Goal reached! Good job!\n${steps - 10000} steps over the goal!`) 
            : console.log(`${10000 - steps} more steps to reach goal.`);
            break;
        }
        steps += Number(command);
        if (steps >= 10000) {
            console.log(`Goal reached! Good job!\n${steps - 10000} steps over the goal!`);
            break;
        }
    }
}

solution(["1000",
"1500",
"2000",
"6500"])

// Goal reached! Good job!
// 1000 steps over the goal!

console.log('********************************');

solution(["1500",
"300",
"2500",
"3000",
"Going home",
"200"])

// 2500 more steps to reach goal.
