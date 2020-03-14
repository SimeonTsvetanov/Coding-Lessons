function areaNew(x1, y1, x2, y2) {
    let length = Math.abs(Number(x1) - Number(x2));
    let width = Math.abs(Number(y1) - Number(y2));

    let area = (length * width).toFixed(2);
    let peremeter = (2 * (length + width)).toFixed(2);

    console.log(area);
    console.log(peremeter);
}

areaNew(60, 20, 10, 50);
areaNew(30, 40, 70, -10);
areaNew(600.25, 500.75, 100.50, -200.5);


// This is the old way we had to solve the task. Yet still working in Judge:
function area(input) {
    let x1 = Number(input.shift());
    let y1 = Number(input.shift());
    let x2 = Number(input.shift());
    let y2 = Number(input.shift());

    let length = Math.abs(x1 - x2);
    let width = Math.abs(y1 - y2);

    let area = (length * width).toFixed(2);
    let peremeter = (2 * (length + width)).toFixed(2);

    console.log(area);
    console.log(peremeter);
}

area(["60", "20", "10", "50"]);
area(["30", "40", "70", "-10"]);
area(["600.25", "500.75", "100.50", "-200.5"]);
