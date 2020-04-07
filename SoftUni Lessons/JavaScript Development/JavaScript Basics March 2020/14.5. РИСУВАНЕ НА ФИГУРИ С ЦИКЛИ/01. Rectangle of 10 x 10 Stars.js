function rect10by10(input) {
    // Mask
    for (let row = 1; row <= 10; row += 1) {
        let result = "";
        for (col = 1; col <= 10; col += 1) {
            result += "*";
        }
        console.log(result);
    }
}

rect10by10();  // Should return:
// **********
// **********
// **********
// **********
// **********
// **********
// **********
// **********
// **********
// **********
