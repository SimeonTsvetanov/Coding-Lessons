function printAndSum(start, end) {
    // Mask
    let sum = 0;
    let result = '';

    for (let num = start; num <= end; num += 1) {
        result += `${num} `;
        sum += num 
    }

    console.log(result);
    console.log(`Sum: ${sum}`);
}

printAndSum(5, 10);  // Should return:
// 5 6 7 8 9 10
// Sum: 45

printAndSum(0, 26);  // Should return:
// 0 1 2 … 26
// Sum: 351
