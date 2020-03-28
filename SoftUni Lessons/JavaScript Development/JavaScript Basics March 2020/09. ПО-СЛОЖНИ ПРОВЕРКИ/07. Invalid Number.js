function invalidNumber(...input) {
    number = Number(input.shift());
    if ((number >= 100 && number <= 200) || number === 0) {
    } else {
        console.log("invalid");
    }
}

invalidNumber(['75']);  // Expected Output: invalid
invalidNumber(['150']);  // Expected Output: (няма изход)
invalidNumber(['220']);  // Expected Output: invalid
invalidNumber(['199']);  // Expected Output: (няма изход)
invalidNumber(['-1']);  // Expected Output: invalid
invalidNumber(['100']);  // Expected Output: (няма изход)
invalidNumber(['200']);  // Expected Output: (няма изход)
invalidNumber(['0']);  // Expected Output: (няма изход)