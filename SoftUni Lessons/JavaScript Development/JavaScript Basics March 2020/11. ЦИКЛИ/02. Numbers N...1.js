function nToOne(...number) {
    number = number.shift()
    for (number; number >= 1; number--) {
        console.log(number);
    }
}

nToOne(3);  // Expected Output: 3 / 2 / 1 "each on a new line".
