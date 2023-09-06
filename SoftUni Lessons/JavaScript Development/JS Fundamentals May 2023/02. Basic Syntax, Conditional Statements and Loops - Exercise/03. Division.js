function mask (params) {
    // MASK
    let num = params;
    let divisors = [2, 3, 6, 7, 10];
    let result = 'Not divisible';

    for (const divisor of divisors) {
        (num % divisor === 0) ? result = `The number is divisible by ${divisor}` : 'pass';
    }

    console.log(result);
}

mask(30);
// The number is divisible by 10

mask(15);
// The number is divisible by 3

mask(1643);
// Not divisible
