function mask (params) {
    // MASK
    let sum_even = params             // receives an array of strings
        .map(Number)                  // parse them into numbers
        .filter(x => x % 2 === 0)     // filter only the even numbers
        .reduce((a, b) => a + b, 0);  // sum the filtered numbers

    console.log(sum_even);
}

mask(['1','2','3','4','5','6'] );
// 12

mask(['3','5','7','9'] );
// 0
