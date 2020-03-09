function evenOrOdd(input) {
    number = Number(input.shift());
    if (number % 2 === 0) {
        console.log("even")
    }
    else {
        console.log("odd")
    }
}

evenOrOdd([2]); // Expected output: even
evenOrOdd([3]); // Expected output: odd
evenOrOdd([25]); // Expected output: odd
evenOrOdd([1024]); // Expected output: even
