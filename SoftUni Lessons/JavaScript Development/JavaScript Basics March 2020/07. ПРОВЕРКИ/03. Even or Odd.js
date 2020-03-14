// There are two ways of reading the Input for this tasks:
// This is the new way:
function evenOrOdd(number) {
    if (number % 2 === 0) {
        console.log("even")
    } else {
        console.log("odd")
    }
}

evenOrOdd(2); // Expected output: even
evenOrOdd(3); // Expected output: odd
evenOrOdd(25); // Expected output: odd
evenOrOdd(1024); // Expected output: even


// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function evenOrOddOld(input) {
    number = Number(input.shift());
    if (number % 2 === 0) {
        console.log("even")
    } else {
        console.log("odd")
    }
}

evenOrOddOld([2]); // Expected output: even
evenOrOddOld([3]); // Expected output: odd
evenOrOddOld([25]); // Expected output: odd
evenOrOddOld([1024]); // Expected output: even
