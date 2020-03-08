function trapezoidArea(input) {
    let b1 = Number(input.shift());
    let b2 = Number(input.shift());
    let h = Number(input.shift());
    let area = (b1 + b2) * h / 2;
    // toFixed(2) wasnt in the desription but in Judge is needed
    console.log(area.toFixed(2));
}

trapezoidArea([8, 13, 7]);  // Expected output: 73.50
