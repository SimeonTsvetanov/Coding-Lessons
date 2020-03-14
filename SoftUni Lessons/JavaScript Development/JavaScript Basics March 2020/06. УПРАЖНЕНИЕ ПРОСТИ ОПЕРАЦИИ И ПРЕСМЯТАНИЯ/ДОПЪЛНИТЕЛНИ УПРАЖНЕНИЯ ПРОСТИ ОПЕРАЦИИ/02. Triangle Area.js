// New way of reading the input:
function triangleArea(a, h) {
    let area = (a * h / 2).toFixed(2)
    console.log(area)
} 

triangleArea(20, 30);  // Expected putput: 300.00
triangleArea(15, 35);  // Expected output: 262.50
triangleArea(7.75, 8.45);  // Expected output: 32.74
triangleArea(1.23456, 4.56789);  // Expected output: 2.82


//------------------------------------------------------------------------------------//
// Old way of reading the input:
function triangleAreaOld(input) {
    let a = Number(input.shift());
    let h = Number(input.shift());
    let area = (a * h / 2).toFixed(2)
    console.log(area)
} 

triangleAreaOld([20, 30]);  // Expected putput: 300.00
triangleAreaOld([15, 35]);  // Expected output: 262.50
triangleAreaOld([7.75, 8.45]);  // Expected output: 32.74
triangleAreaOld([1.23456, 4.56789]);  // Expected output: 2.82
