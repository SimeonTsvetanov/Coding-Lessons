function calculator (...args) {
    let a = args.shift();
    let operator = args.shift();
    let b = args.shift();
    let result = 0;

    switch (operator) {
        case '+':
            result = a + b;
            break;
        case '-':
            result = a - b;
            break;
        case '*':
            result = a * b;
            break;
        case '/':
            result = a / b;
            break;
    }

    console.log(result.toFixed(2));
}

calculator(5, "+", 10);