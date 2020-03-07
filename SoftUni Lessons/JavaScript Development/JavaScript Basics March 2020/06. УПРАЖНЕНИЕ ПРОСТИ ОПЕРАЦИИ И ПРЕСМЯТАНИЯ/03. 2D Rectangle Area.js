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
