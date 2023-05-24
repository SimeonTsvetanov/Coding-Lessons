function solution(params) {
    // MasK
    let num = Number(params.shift());
    let specialNumbers = [];
    

    for (let i = 1111; i <= 9999; i++) {
        let check = [];
        
        for (let j = 0; j < 4; j++) {
            check.push(num % Number(String(i)[j]) == 0);
        }
        
        (check.every(x => (x))) ? specialNumbers.push(i) : 'pass';
    }

    console.log(specialNumbers.join(' '));
}

solution(["3"]);
// 1111 1113 1131 1133 1311 1313 1331 1333 3111 3113 3131 3133 3311 3313 3331 3333

console.log('********************************');

solution(["11"]);
// 1111