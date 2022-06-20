function numberModification (num) {
    // MasK
    num = num.toString().split('').map(Number);

    while ('the average value of all its digits is higher than 5') {
        if ((num.reduce((a, b) => a + b, 0)) / num.length > 5) {
            console.log(num.join(''));
            break;
        }

        num.push(9);
    }
}

numberModification(101);  // 1019999
numberModification(5835);  // 5835
