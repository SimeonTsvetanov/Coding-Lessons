function primeNumberChecker(num) {
    // Mask
    let prime = true;
    for(let i = 2; i <= num - 1; i++)
        if (num % i === 0) {
            prime = false;
            break;
        }
    console.log(prime);
}

primeNumberChecker(7);  // Should return: true

primeNumberChecker(8);  // Should return: false