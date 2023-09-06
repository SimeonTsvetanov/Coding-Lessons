function mask (x1, y1, x2, y2) {
    // MASK
    // console.log(Math.hypot(x2-x1, y2-y1).);  // This should work BUT judge don't like more than 13 symbols

    // So the solution that works is:
    let x = Math.abs(x1 - x2);
    let y = Math.abs(y1 - y2);
    let distance = Math.sqrt(x * x + y * y);
    console.log(distance);
}

mask(2, 4, 5, 0);
//

mask(2.34, 15.66, -13.55, -2.9985);
//
