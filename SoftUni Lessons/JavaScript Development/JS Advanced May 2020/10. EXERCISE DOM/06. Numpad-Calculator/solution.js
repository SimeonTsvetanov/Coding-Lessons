function solve() {
    // Lets Get all the buttons in one Array:
    let buttons = document.querySelector('.keys');
    // Get the expression Output area:
    let expressionOutput = document.querySelector('#expressionOutput');
    // Get the Result Output area:
    let resultOutput = document.querySelector('#resultOutput');
    // Get the Clear button:
    let clearButton = document.querySelector('.clear');
    
    // Set the Buttons Listener in a loop for Expression:
    let expression = '';
    buttons.addEventListener('click', click => {
        let value = click.target.value;
        
        if (value !== '=') {
            if (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'].includes(value)) {
                // Operand or decimal point is pressed:                
                expression += `${value}`
                expressionOutput.innerText = expression;
            } else {
                // Operator is pressed
                expression += ` ${value} `;
                expressionOutput.innerText = expression;
            }
        } else {
            // Equal Sign Pressed
            try {
                // Two ways of solving:
                // First (NOT USED without eval:)
                let [numOne, operator, numTwo] = expression.split(' ');
                let resultNotEval = {'-': (a, b) => a - b, '+': (a, b) => a + b, '*': (a, b) => a * b, '/': (a, b) => a / b}[operator](Number(numOne), Number(numTwo));
                console.log(resultNotEval);  // --> Just to see that it's working in the console.
                
                // Second USED with EVAL: 
                let result = eval(expression);
                resultOutput.innerText = result;  // Change it to resultNotEval and it will use the first method.
            } catch (error) {
                resultOutput.innerText = 'NaN';
            }
        }
    })

    // Set the listener for the Clear Button:
    clearButton.addEventListener('click', e => {
        // console.log(e.target); // - to get the button target <<<
        // Big brush commin' :D
        resultOutput.innerText = '';
        expression = '';
        expressionOutput.innerText = '';
    })
}
