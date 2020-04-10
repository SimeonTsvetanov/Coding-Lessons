function sumPrimeNotPrime(input) {
    // Mask
    // This task was ugly as fuck. 
    let primes = 0;
    let notPrimes = 0;

    while('command is stop') {
        let isPrime = true;

        let command = input.shift();
        if (command == 'stop') {
            break;
        }
        let num = Number(command);

        if (num < 0) {
            console.log(`Number is negative.`);
            continue
        }
        if (num == 0 || num == 1) {
            notPrimes += num;
            continue
        }
        
        for(i = 2; i <= num - 1; i++) {
            if (num % i == 0) { 
                isPrime = false; 
                break; 
            }
        }

        if (isPrime) {primes += num}
        else {notPrimes += num}
    }

    console.log(`Sum of all prime numbers is: ${primes}`);
    console.log(`Sum of all non prime numbers is: ${notPrimes}`);
}

sumPrimeNotPrime([3, 9, 0, 7, 19, 4, 'stop']);  // Should return:
// Sum of all prime numbers is: 29
// Sum of all non prime numbers is: 13

sumPrimeNotPrime([30, 83, 33, -1, 20, 'stop']);  // Should return:
// Number is negative.
// Sum of all prime numbers is: 83
// Sum of all non prime numbers is: 83
