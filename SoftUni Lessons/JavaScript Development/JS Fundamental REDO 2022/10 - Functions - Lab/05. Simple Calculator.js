function simpleCalc (num1, num2, operator) {
    // MasK
    let result = {
        'multiply': (a, b) => {return a * b},
        'divide': (a, b) => {return a / b},
        'add': (a, b) => {return a + b},
        'subtract': (a, b) => {return a - b}
    }[operator](num1, num2);

    console.log(result);
}

simpleCalc(5, 5, 'multiply');  // 25