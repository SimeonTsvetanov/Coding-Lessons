// Write a function that returns the English name of the last digit of a given number.
// Write a program that receives a number and prints the returned value from this function.

function lastDigit(number) {
    let lastDigit = number % 10;
    const lastDigitNames = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'};
    console.log(lastDigitNames[lastDigit]);
}

lastDigit(512);