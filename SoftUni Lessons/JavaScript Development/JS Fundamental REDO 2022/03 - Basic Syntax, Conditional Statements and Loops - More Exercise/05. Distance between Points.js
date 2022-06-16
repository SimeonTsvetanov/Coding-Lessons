// Write a JS function that calculates the distance between two points by given x and y coordinates.
// The input comes as four number elements in the format x1, y1, x2, y2.
// Each pair of elements are the coordinates of a point in 2D space.
// The output should be returned as a result of your function.

function distance(x1, y1, x2, y2) {
    let x = Math.abs(x1 - x2);
    let y = Math.abs(y1 - y2);
    let distance = Math.sqrt(x * x + y * y);
    console.log(distance);
}

distance(2.34, 15.66, -13.55, -2.9985);

