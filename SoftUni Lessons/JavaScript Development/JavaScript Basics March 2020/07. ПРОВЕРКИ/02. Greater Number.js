function greaterNumber(input) {
    numOne = Number(input.shift());
    numTwo = Number(input.shift());
    
    if (numOne > numTwo) {
        console.log(numOne);
    } 
    else {
        console.log(numTwo);
    }
}

greaterNumber([5, 3]);  // Expected output: 5
greaterNumber([3, 5]);  // Expected output: 5
greaterNumber([10, 10]);  // Expected output: 10
greaterNumber([-5, 5]);  // Expected output: 5
