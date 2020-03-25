function repainting(params) {
    plastic = (Number(params.shift()) + 2) * 1.5;
    paint = (Number(params.shift()) * 1.1) * 14.50;
    primer = Number(params.shift()) * 5;
    hours = Number(params.shift());

    let materials = plastic + paint + primer + 0.4;
    let work = (materials * 0.3) * hours;

    let total = materials + work;

    console.log(`Total expenses: ${total.toFixed(2)} lv.`);
}


repainting([10, 11, 4, 8])  // Expected Output:
// Total expenses: 727.09 lv.

repainting([5, 10, 10, 1])  // Expected Output:
// Total expenses: 286.52 lv.

repainting([90, 99, 28, 9])  // Expected Output:
// Total expenses: 6872.57 lv.