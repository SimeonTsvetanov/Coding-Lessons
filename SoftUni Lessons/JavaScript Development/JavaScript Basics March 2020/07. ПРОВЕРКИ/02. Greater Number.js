// There are two ways of reading the Input for this tasks:
// This is the new way:
function greaterNumber(numOne, numTwo) {
    if (numOne > numTwo) {
        console.log(numOne);
    } else {
        console.log(numTwo);
    }
}

greaterNumber(5, 3);  // Expected output: 5
greaterNumber(3, 5);  // Expected output: 5
greaterNumber(10, 10);  // Expected output: 10
greaterNumber(-5, 5);  // Expected output: 5


// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function OldgreaterNumber(input) {
    numOne = Number(input.shift());
    numTwo = Number(input.shift());
    
    if (numOne > numTwo) {
        console.log(numOne);
    } else {
        console.log(numTwo);
    }
}

OldgreaterNumber([5, 3]);  // Expected output: 5
OldgreaterNumber([3, 5]);  // Expected output: 5
OldgreaterNumber([10, 10]);  // Expected output: 10
OldgreaterNumber([-5, 5]);  // Expected output: 5
