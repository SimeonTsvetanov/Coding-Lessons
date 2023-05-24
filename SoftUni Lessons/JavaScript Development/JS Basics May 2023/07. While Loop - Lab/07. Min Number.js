function solution(params) {
    // MasK
    let min = Number.MAX_SAFE_INTEGER;

    while ('i say so!') {
        num = params.shift();
        if (num === 'Stop') {
            console.log(min);
            break;
        }
        if (Number(num) <= min) {
            min = Number(num);
        }
    }
}

solution(["100",
"99",
"80",
"70",
"Stop"])

// 70

console.log('********************************');

solution(["-10",
"20",
"-30",
"Stop"])

// -30