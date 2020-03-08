function housePainting(input) {
    let x = Number(input.shift());
    let y = Number(input.shift());
    let h = Number(input.shift());

    let greenPaint = ((((2 * (x * y)) - (4.5)) + ((2 * (x * x)) - 2.4)) / 3.4).toFixed(2);
    let redPaint = (((2 * (x * y)) + (2 * ((x * h) / 2))) / 4.3).toFixed(2);

    console.log(greenPaint);
    console.log(redPaint);
}

housePainting([6, 10, 5.2]);  // Expected output: 54.44 ... 35.16
housePainting([10.25, 15.45, 8.88]);  // Expected output: 152.93 ... 94.82