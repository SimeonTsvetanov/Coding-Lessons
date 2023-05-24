function solution(params) {
    // MasK
    let n = Number(params.shift());
    let curr = 1;

    while (curr <= n) {
        console.log(curr);
        curr = (curr * 2) + 1;
    }
}

solution(["3"])
// 1
// 3


console.log('********************************');

solution(["8"])
// 1
// 3
// 7
// 15
