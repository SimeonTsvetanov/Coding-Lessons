function circleAreaAndPerimeter(input) {
    let radius = Number(input.shift());

    let area = (Math.PI * radius * radius).toFixed(2);
    let perimeter = (2 * Math.PI * radius).toFixed(2);
    
    console.log(area);
    console.log(perimeter);
}

circleAreaAndPerimeter([3]);  // Expected output: 28.27 / 18.85
circleAreaAndPerimeter([4.5]);  // Expected output: 63.62 / 28.27