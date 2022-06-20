function processOddNumbers (arr) {
    // MasK
    let result = [];

    arr.forEach((num, index) => {
        index % 2 !== 0 ? result.push(num * 2) : 'pass';
    });

    console.log(result.reverse().join(' '));
}

processOddNumbers([10, 15, 20, 25]);  // 50 30