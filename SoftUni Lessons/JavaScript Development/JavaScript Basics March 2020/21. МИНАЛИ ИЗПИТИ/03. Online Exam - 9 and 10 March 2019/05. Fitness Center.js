function fitnessCenter(input) {
    // Mask
    let ac = {
        'Back': 0,
        'Chest': 0,
        'Legs': 0,
        'Abs': 0,
        'Protein shake': 0,
        'Protein bar': 0
    };

    let acts = Number(input.shift());

    for (let act = 1; act <= acts; act += 1) {
        ac[input.shift()] += 1;
    }

    let training = ac['Back'] + ac['Chest'] + ac['Legs'] + ac['Abs'];
    let suppliments = ac['Protein shake'] + ac['Protein bar'];

    console.log(`${ac['Back']} - back`);
    console.log(`${ac['Chest']} - chest`);
    console.log(`${ac['Legs']} - legs`);
    console.log(`${ac['Abs']} - abs`);
    console.log(`${ac['Protein shake']} - protein shake`);
    console.log(`${ac['Protein bar']} - protein bar`);
    console.log(`${(training / acts * 100).toFixed(2)}% - work out`);
    console.log(`${(suppliments / acts * 100).toFixed(2)}% - protein`);
}

fitnessCenter([10, 'Back', 'Chest', 'Legs', 'Abs', 'Protein shake', 'Protein bar', 'Protein shake', 'Protein bar', 'Legs', 'Abs']);  
// Should return:
// 1 - back
// 1 - chest
// 2 - legs
// 2 - abs
// 2 - protein shake
// 2 - protein bar
// 60.00% - work out
// 40.00% - protein

fitnessCenter([7, 'Chest', 'Back', 'Legs', 'Legs', 'Abs', 'Protein shake', 'Protein bar']);  
// Should return:
// 1 - back
// 1 - chest
// 2 - legs
// 1 - abs
// 1 - protein shake
// 1 - protein bar
// 71.43% - work out
// 28.57% - protein
