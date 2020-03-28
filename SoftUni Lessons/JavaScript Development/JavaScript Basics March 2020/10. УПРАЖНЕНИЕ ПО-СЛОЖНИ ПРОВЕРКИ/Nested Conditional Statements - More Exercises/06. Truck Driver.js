function truckDriver(...input) {
    let season = input.shift();  // "Spring", "Summer", "Autumn" or "Winter"
    let kilometers = Number(input.shift());

    let wage = undefined;

    if (kilometers <= 5000) {
        wage = ((({'Spring' :0.75, 'Autumn': 0.75, 'Summer': 0.9, 'Winter': 1.05}[season]) * kilometers) * 4) * 0.9;
    } else if (kilometers > 5000 && kilometers <= 10000) {
        wage = ((({'Spring' :0.95, 'Autumn': 0.95, 'Summer': 1.1, 'Winter': 1.25}[season]) * kilometers) * 4) * 0.9;
    } else if (kilometers > 10000 && kilometers <= 20000) {
        wage = ((1.45 * kilometers) * 4) * 0.9;
    }

    console.log(wage.toFixed(2));
}


truckDriver(['Summer', '3455']);  // Expected Output: 11194.20
truckDriver(['Winter', '4350']);  // Expected Output: 16443.00
truckDriver(['Spring', '1600']);  // Expected Output: 4320.00
truckDriver(['Winter', '5678']);  // Expected Output: 25551.00
truckDriver(['Autumn', '8600']);  // Expected Output: 29412.00
truckDriver(['Winter', '16042']);  // Expected Output: 83739.24
truckDriver(['Spring', '16942']);  // Expected Output: 88437.24
