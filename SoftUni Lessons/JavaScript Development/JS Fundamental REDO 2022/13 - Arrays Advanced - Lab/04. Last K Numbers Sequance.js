function lastKNumbers (n, k) {
    // MasK
    let result = [];

    for (let i = 0; i < n; i++) {
        if (result.length === 0) {
            result.push(1);
            continue;
        }
        let start = i - k > 0 ? i - k : 0;
        let end = i
        let lastThree = result.slice(start, end);
        let sum = lastThree.reduce((a, b) => a + b, 0);
        result.push(sum);
    }

    console.log(result.join(' '));
}

lastKNumbers(6, 3);  // 1 1 2 4 7 13
lastKNumbers(8, 2);  // 1 1 2 3 5 8 13 21