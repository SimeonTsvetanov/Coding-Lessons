function calculator(numOne, operator, numTwo) {
    // Mask
    console.log(eval(`${numOne} ${operator} ${numTwo}`).toFixed(2));
}

calculator(5, '+', 10); // Should Return: 15
