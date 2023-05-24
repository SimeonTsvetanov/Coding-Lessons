function solution(params) {
    // MasK
    let [start, end, magic] = [Number(params.shift()), Number(params.shift()), Number(params.shift())];
    let combination = 0;
    let happy = false;
    
    for (let a = start; a <= end; a++) {
        if (happy) {break;}
        for (let b = start; b <= end; b++) {
            combination++;
            if (a + b == magic) {
                happy = `Combination N:${combination} (${a} + ${b} = ${magic})`;
                break;
            }
        }
    }
    (!happy) ? console.log(`${combination} combinations - neither equals ${magic}`) : console.log(happy);;
}

solution(["1",
"10",
"5"])

// Combination N:4 (1 + 4 = 5)

console.log('********************************');

solution(["23",
"24",
"20"])

// 4 combinations - neither equals 20