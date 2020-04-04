function sumOfSeries(...input) {
    // Mask
    let number = Number(input.shift());
    
    let total = 0

    for (let i = 1; i <= number; i++) {
        total += (i * i)
    }

    console.log(total);
}

sumOfSeries(7);  // Should return: 140
