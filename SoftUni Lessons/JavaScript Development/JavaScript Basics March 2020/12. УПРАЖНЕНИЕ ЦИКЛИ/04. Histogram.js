function histogram(params) {
    let groupOne = 0;  // < 200
    let groupTwo = 0;  // 200 … 399
    let groupThree = 0;  // 400 … 599
    let groupFour = 0;  // 600 … 799
    let groupFive = 0;  // ≥ 800

    let countNumbers = Number(params.shift());
    
    for (let time = 1; time <= countNumbers; time++) {
        let num = Number(params.shift());

        if (num < 200) {groupOne += 1;}
        else if (num >= 200 && num <= 399) {groupTwo += 1;}
        else if (num >= 400 && num <= 599) {groupThree += 1;}
        else if (num >= 600 && num <= 799) {groupFour += 1;}
        else if (num >= 800) {groupFive += 1;}
    }

    console.log(`${(groupOne / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupTwo / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupThree / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupFour / countNumbers * 100).toFixed(2)}%`);
    console.log(`${(groupFive / countNumbers * 100).toFixed(2)}%`);
}


histogram([3, 1, 2, 999]);  // Expected Output:
// 66.67%
// 0.00%
// 0.00%
// 0.00%
// 33.33%

histogram([4, 53, 7, 56, 999]);  // Expected Output:
// 75.00%
// 0.00%
// 0.00%
// 0.00%
// 25.00%


