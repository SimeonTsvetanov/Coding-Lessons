function processOddNumbers(array) {
    // Mask

    function methodOne (array) {
        let result = [];
        array.map((number, index) => {
            index % 2 !== 0 ? result.unshift(number * 2) : 'pass';
        });
        console.log(...result)
    }

    function methodTwo(array) {
        let result = array
            .filter((num, i) => i % 2 === 1)
            .map(x => x * 2)
            .reverse();
        console.log(...result);
    }

    // methodOne(array);
    methodTwo(array);
}

processOddNumbers([10, 15, 20, 25]);  // Should return: 50 30

processOddNumbers([3, 0, 10, 4, 7, 3]);  // Should return: 6 8 0