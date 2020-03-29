// Not included in final score
function moving(data) {
    let free = Number(data.shift()) * Number(data.shift()) * Number(data.shift());
    let used = 0;

    while('Done or No more Sprace') {
        boxes = data.shift();
        if (boxes == 'Done') {break;}
        used += Number(boxes);
        if(used >= free) {break;}
    }

    if (used < free) {console.log(`${free - used} Cubic meters left.`);}
    else {console.log(`No more free space! You need ${used - free} Cubic meters more.`);}
}

moving([10, 10, 2, 20, 20, 20, 20, 122]);  // Expected Output:
// No more free space! You need 2 Cubic meters more.

moving([10, 1, 2, 4, 6, 'Done']);  // Expected output:
// 10 Cubic meters left.
