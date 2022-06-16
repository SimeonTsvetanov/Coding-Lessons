function divisible_by(num) {
    let result = undefined
    for (const x of [2, 3, 6, 7, 10]) {
        num % x === 0 ? result = x : 'pass'
    }

    result ? console.log(`The number is divisible by ${result}`) : console.log('Not divisible');
}

divisible_by(30);
divisible_by(15);
divisible_by(12);
divisible_by(1643);


