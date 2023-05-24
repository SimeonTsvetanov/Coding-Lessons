function solution(params) {
    // MasK
    let n = Number(params.shift());
    let stop = false
    let num = 1

    for (let rows = 1; rows <= n; rows++) {
        if (stop) {break;}
        let line = ''
        for (let col = 1; col <= rows; col++) {
            line += `${num} `
            if (num == n) {stop = true; break;}
            num ++
        }
        console.log(line)
    }
}

solution(["7"]);
// 1
// 2 3
// 4 5 6 
// 7

console.log('********************************');

solution(["12"]);
// 1
// 2 3
// 4 5 6
// 7 8 9 10 
// 11 12