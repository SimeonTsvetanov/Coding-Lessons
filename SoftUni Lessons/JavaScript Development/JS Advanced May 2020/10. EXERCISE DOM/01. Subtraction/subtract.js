function subtract() {
    // Get the Numbers:
    let numOne = Number(document.querySelector('#firstNumber').value);
    let numTwo = Number(document.querySelector('#secondNumber').value);
    
    // Set the Result:
    document.querySelector('#result').textContent = numOne - numTwo;
}
