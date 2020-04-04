function leftAndRightSum(...params) {
    let times = Number(params.shift());
    
    let leftSum = 0;
    let rightSum = 0;
    
    for (i = 1; i <= times; i++) {
        leftSum += Number(params.shift());
    }

    for (i = 1; i <= times; i++) {
        rightSum += Number(params.shift());
    }

    if (leftSum == rightSum) {
        console.log(`Yes, sum = ${leftSum}`);
    } else {
        console.log(`No, diff = ${Math.abs(leftSum - rightSum)}`)
    }
}

leftAndRightSum(2, 10, 90, 60, 40);  // Expected Output: Yes, sum = 100
leftAndRightSum(2, 90, 9, 50, 50);  // Expected Output: No, diff = 1

