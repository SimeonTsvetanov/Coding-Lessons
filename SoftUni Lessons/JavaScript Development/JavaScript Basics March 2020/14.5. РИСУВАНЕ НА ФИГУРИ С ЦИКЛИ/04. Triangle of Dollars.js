function tiangleOfDollars(input) {
    // Mask
    let n = Number(input.shift());
    for (let row = 1; row <= n; row += 1) {
        let result = "";
        for (let col = 1; col <= row; col += 1) {
            result += "$ "
        }
        console.log(result);
    }
}

tiangleOfDollars([2]);  // Should return:
// $
// $$ 

tiangleOfDollars([3]);  // Should return:
// $
// $$
// $$$
