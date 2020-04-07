function rectNbyNSpace(input) {
    // Mask
    let n = Number(input.shift());
    for (let row = 1; row <= n; row += 1) {
        let result = "";
        for (col = 1; col <= n; col += 1) {
            result += "* ";
        }
        console.log(result);
    }
}

rectNbyNSpace([2]);  // Should return:
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