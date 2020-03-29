function devideWithoutRemainder(params) {
    let groupOne = 0;  // num % 2 == 0
    let groupTwo = 0;  // num % 3 == 0
    let groupThree = 0;  // num % 4 == 0

    let countNumbers = Number(params.shift());
    
    for (let time = 1; time <= countNumbers; time++) {
        let num = Number(params.shift());

        if (num % 2 == 0) {groupOne += 1;}
        if (num % 3 == 0) {groupTwo += 1;}
        if (num % 4 == 0) {groupThree += 1;}
    }

    console.log(`${(groupOne / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupTwo / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupThree / countNumbers * 100).toFixed(2)}%`);
}

devideWithoutRemainder([10, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65]);
// Expected output:
// 70.00%
// 10.00%
// 50.00%

devideWithoutRemainder([3, 3, 6, 9]);
// Expected Output:
// 33.33%
// 100.00%
// 0.00%
