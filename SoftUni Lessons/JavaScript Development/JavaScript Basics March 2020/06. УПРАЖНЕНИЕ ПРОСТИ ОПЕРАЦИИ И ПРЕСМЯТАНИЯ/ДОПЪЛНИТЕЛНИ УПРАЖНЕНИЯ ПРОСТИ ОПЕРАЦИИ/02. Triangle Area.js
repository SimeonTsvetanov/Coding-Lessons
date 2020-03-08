function triangleArea(input) {
    let a = Number(input.shift());
    let h = Number(input.shift());
    let area = (a * h / 2).toFixed(2)
    console.log(area)
} 

triangleArea([20, 30]);  // Expected putput: 300.00
triangleArea([15, 35]);  // Expected output: 262.50
triangleArea([7.75, 8.45]);  // Expected output: 32.74
triangleArea([1.23456, 4.56789]);  // Expected output: 2.82
