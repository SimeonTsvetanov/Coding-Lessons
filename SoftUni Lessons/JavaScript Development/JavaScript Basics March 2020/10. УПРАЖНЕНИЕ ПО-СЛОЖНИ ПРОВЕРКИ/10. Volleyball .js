// Not included in final score
function volleyball(...input) {
    let y = input.shift();
    let p = Number(input.shift());
    let h = Number(input.shift());
    let g = (((48 - h) * 3 / 4) + h) + (p * (2 / 3));
    if (y == "leap") {g += g * 0.15}
    console.log(Math.floor(g));
}

volleyball(['leap', '5', '2']);  // Expected Output: 45
volleyball(['normal', '3', '2']);  // Expected Output: 38
volleyball(['leap', '2', '3']);  // Expected Output: 43
volleyball(['normal', '11', '6']);  // Expected Output: 44
volleyball(['leap', '0', '1']);  // Expected Output: 41
volleyball(['normal', '6', '13']);  // Expected Output: 43
