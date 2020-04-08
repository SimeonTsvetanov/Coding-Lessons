function easterEggs(input) {
    // Mask
    let colors = { 
        'red': 0,
        'orange': 0,
        'blue': 0,
        'green': 0
    };

    let maxColor = undefined;
    let maxCount = 0;

    let count = Number(input.shift());

    for (let time = 1; time <= count; time += 1) {
        let color = input.shift();
        colors[color] += 1;
        if (colors[color] > maxCount) {
            maxCount = colors[color];
            maxColor = color;
        }
    }

    console.log(`Red eggs: ${colors['red']}`);
    console.log(`Orange eggs: ${colors['orange']}`);
    console.log(`Blue eggs: ${colors['blue']}`);
    console.log(`Green eggs: ${colors['green']}`);
    console.log(`Max eggs: ${maxCount} -> ${maxColor}`)
}

easterEggs([7, 'orange', 'blue', 'green', 'green', 'blue', 'red', 'green']);  // Should return:
// Red eggs: 1
// Orange eggs: 1
// Blue eggs: 2
// Green eggs: 3
// Max eggs: 3 -> green

easterEggs([4, 'blue', 'red', 'blue', 'orange']);  // Should return:
// Red eggs: 1
// Orange eggs: 1
// Blue eggs: 2
// Green eggs: 0
// Max eggs: 2 -> blue
