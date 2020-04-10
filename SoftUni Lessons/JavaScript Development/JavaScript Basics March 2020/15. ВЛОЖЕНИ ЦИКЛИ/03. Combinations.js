function combinaions(input) {
    // Mask
    
    let valid = 0

    let n = Number(input.shift());
    for (let x1 = 0; x1 <= n; x1++) {
        for (let x2 = 0; x2 <= n; x2++) {
            for (let x3 = 0; x3 <= n; x3++) {
                if ((x1 + x2 + x3) == n) {valid += 1;}
            } 
        } 
    }

    console.log(valid);
}

combinaions([25]);  // Should return: 351

combinaions([20]);  // Should return: 231