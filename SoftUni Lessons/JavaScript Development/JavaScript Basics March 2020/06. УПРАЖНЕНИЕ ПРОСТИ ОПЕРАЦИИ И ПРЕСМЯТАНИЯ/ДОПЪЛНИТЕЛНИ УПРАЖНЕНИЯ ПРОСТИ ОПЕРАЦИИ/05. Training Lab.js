// There are two ways to test the task in Judge
// This is the new way:
function trainingLab(width, height) {
    // To get the devision without remaining 
    // We can use Math.floor() but if we have negative numbers it will break :D
    // So from now on I'll try to use ~~(num1 / num2) instead:
    let spaces_width = ~~(height / 70);  
    let spaces_heigth = ~~(width / 120); 
    
    let spaces = (spaces_width * spaces_heigth) - 3;
    console.log(spaces);
}

trainingLab(15, 8.9);  // Expected output: 129
trainingLab(8.4, 5.2);  // Expected output: 39


// -----------------------------------------------------------------------------------//
// Old way of reading the input:
function trainingLabOld(input) {
    let width = (Number(input.shift()) * 100);
    let height = (Number(input.shift()) * 100) - 100;
    
    let spaces_width = ~~(height / 70);  
    let spaces_heigth = ~~(width / 120); 
    
    let spaces = (spaces_width * spaces_heigth) - 3;
    console.log(spaces);
}

trainingLabOld([15, 8.9]);  // Expected output: 129
trainingLabOld([8.4, 5.2]);  // Expected output: 39