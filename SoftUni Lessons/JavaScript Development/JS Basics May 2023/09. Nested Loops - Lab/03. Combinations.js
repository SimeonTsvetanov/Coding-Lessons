function solution(params) {
    // MasK
    let num = Number(params.shift());
    let valid = 0;

    for (let a = 0; a <= num; a++) {
        for (let b = 0; b <= num; b++) {
            for (let c = 0; c <= num; c++) {
                if (a + b + c === num) {
                    valid++;
                }
            }    
        }
    }

    console.log(valid);
}

solution(["25"])
// 351

console.log('********************************');

solution(["20"])
// 231