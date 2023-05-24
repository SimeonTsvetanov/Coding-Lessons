function numbersDevisibleByNine(params) {
    let start = Number(params.shift());
    let end = Number(params.shift())
    
    let nums = [];

    for (let num = start; num <= end; num++) {
        if (num % 9 == 0) {
            nums.push(num);
        }
    }

    let sum = nums.reduce((a, b) => a + b, 0);

    console.log(`The sum: ${sum}`);
    nums.forEach(num => console.log(num));
}

numbersDevisibleByNine(["100", "200"]);
// The sum: 1683
// 108
// 117
// 126
// 135
// 144
// 153
// 162
// 171 
// 180 
// 189
// 198
