function averageNumber(params) {
    let count = Number(params.shift());
    let sum = 0;

    let counter = 1;

    while(counter <= count) {
        sum += Number(params.shift());
        counter += 1;
    }

    console.log((sum / count).toFixed(2));
}

averageNumber([4, 3, 2, 4, 2]);  // Expected Output: 2.75
averageNumber([2, 6, 4]);  // Expected Output: 5.00
averageNumber([3, 82, 43, 22]);  // Expected Output: 49.00
averageNumber([4, 95, 23, 76, 23]);  // Expected Output: 54.25
