// There are two ways to test the task in Judge
// This is the new way:
function circleAreaAndPerimeter(radius) {
    let area = (Math.PI * radius * radius).toFixed(2);
    let perimeter = (2 * Math.PI * radius).toFixed(2);
    
    console.log(area);
    console.log(perimeter);
}

circleAreaAndPerimeter(3);  // Expected output: 28.27 / 18.85
circleAreaAndPerimeter(4.5);  // Expected output: 63.62 / 28.27


// -----------------------------------------------------------------------------------//
// Old way of reading the input:
function circleAreaAndPerimeterOld(input) {
    let radius = Number(input.shift());

    let area = (Math.PI * radius * radius).toFixed(2);
    let perimeter = (2 * Math.PI * radius).toFixed(2);
    
    console.log(area);
    console.log(perimeter);
}

circleAreaAndPerimeterOld([3]);  // Expected output: 28.27 / 18.85
circleAreaAndPerimeterOld([4.5]);  // Expected output: 63.62 / 28.27