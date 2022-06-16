function primeNumberchecker (num) {
    // Check if the number is a prime number
    // If it is a prime number, return true
    // If it is not a prime number, return false
    if (num < 2) {
        console.log(false);
    } else {
        for (let i = 2; i < num; i++) {
            if (num % i === 0) {
                console.log(false);
                return;
            }
        }
        console.log(true);
    }
}

primeNumberchecker(7);  // true
primeNumberchecker(8);  // false
primeNumberchecker(81);  // false