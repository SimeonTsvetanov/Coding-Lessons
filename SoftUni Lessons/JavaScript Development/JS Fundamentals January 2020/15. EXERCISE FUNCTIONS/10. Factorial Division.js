function factorialDivision(numOne, numTwo) {
    // Mask

    function getFactorial(num) {
        let factorial = 1;
        for (let i = 1; i <= num; i++){
            factorial = factorial * i;
        }
        return factorial;
    }

    function printDivision(one, two) {
        return console.log(`${(getFactorial(one) / getFactorial(two)).toFixed(2)}`);
    }

    printDivision(numOne, numTwo);
}

factorialDivision(5,2);  // Should return: 60.00

factorialDivision(6,2);  // Should return: 360.00