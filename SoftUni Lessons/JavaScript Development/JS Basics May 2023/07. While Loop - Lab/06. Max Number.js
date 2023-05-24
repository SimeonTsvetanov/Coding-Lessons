function solution(params) {
    // MasK
    let max = Number.MIN_SAFE_INTEGER;

    while ('i say so!') {
        num = params.shift();
        if (num === 'Stop') {
            console.log(max);
            break;
        }
        if (Number(num) >= max) {
            max = Number(num);
        }
    }
}

solution(["100",
"99",
"80",
"70",
"Stop"])

// 100

console.log('********************************');

solution(["-10",
"20",
"-30",
"Stop"])

// 20