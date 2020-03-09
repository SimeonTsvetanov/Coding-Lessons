function AreaOfFigures(input) {
    figure = input.shift();
    area = 0;

    if (figure === "square") {
        let number = Number(input.shift());
        area = number * number;
    }
    else if (figure === "rectangle") {
        let length = Number(input.shift());
        let width = Number(input.shift());
        area = length * width;
    }
    else if (figure === "circle") {
        radius = Number(input.shift());
        area = Math.PI * radius * radius; 
    }
    else if (figure === "triangle") {
        let side = Number(input.shift());
        let height = Number(input.shift());
        area = side * (height / 2);
    }
    
    console.log(area.toFixed(3));
}

AreaOfFigures(['square', 5]) // Expected output: 25.000
AreaOfFigures(['rectangle', 7, 2.5]) // Expected output: 17.500
AreaOfFigures(['circle', 6]) // Expected output: 113.097
AreaOfFigures(['triangle', 4.5, 20]) // Expected output: 45.000
