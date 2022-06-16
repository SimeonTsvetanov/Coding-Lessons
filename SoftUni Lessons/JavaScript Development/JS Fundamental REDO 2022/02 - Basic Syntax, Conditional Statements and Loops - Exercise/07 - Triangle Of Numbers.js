function triangleOfNumbers(n) {
    for (let x = 1; x <= n; x++) {
        console.log(Array.from(Array(x).fill(x)).join(' '));
    }
}


triangleOfNumbers(5);
