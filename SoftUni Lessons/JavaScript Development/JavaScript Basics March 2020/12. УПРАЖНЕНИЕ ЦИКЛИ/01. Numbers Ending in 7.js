function numbersEndingInSeven() {
    for (let number = 7; number <= 1000; number++) {
        if (number % 10 === 7) {
            console.log(number);
        }
    }
}

numbersEndingInSeven();  // Expected Output:
// 7
// 17
// 27
// …
// 997
