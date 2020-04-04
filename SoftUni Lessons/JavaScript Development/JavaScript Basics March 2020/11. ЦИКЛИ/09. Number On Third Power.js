function numberOnThirdPower(...input) {
    // Mask
    n = Number(input.shift());
    if (n % 2 == 0) {
        for (let i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                console.log(`Current number: ${i}. Cube: ${i ** 3}`);
                
            }
        }
    } else if (n % 2 != 0){
        for (let i = 1; i <= n; i++) {
            if (i % 2 != 0) {
                console.log(`Current number: ${i}. Cube: ${i ** 3}`);
                
            }
        }
    }
}

numberOnThirdPower(5);  // Should return:
// Current number: 1. Cube: 1
// Current number: 3. Cube: 27
// Current number: 5. Cube: 125

numberOnThirdPower(6);  // Should return:
// Current number: 2. Cube: 8
// Current number: 4. Cube: 64
// Current number: 6. Cube: 216
