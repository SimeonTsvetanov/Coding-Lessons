// There are two ways to solve this problem as the requerments are different in
// Judge, so I have added the two Functions  :)
function workshopNew(countTables, length, width) {
    let coversArea = countTables * (length + 2 * 0.30) * (width + 2 * 0.30);
    let sqareCoversArea = countTables * (length / 2) * (length / 2);

    let priceUSD = ((coversArea * 7) + (sqareCoversArea * 9));
    let priceBGN = (priceUSD * 1.85);

    // Future Reminder: add the .toFixed only in the print as it tends to mess the calculations.
    console.log(`${priceUSD.toFixed(2)} USD`);
    console.log(`${priceBGN.toFixed(2)} BGN`);
}

workshopNew(5, 1.00, 0.50)
workshopNew(10, 1.20, 0.65)


// This is the old way we had to solve this task: (reading the input is different:)
function workshop(input) {
    let countTables = Number(input.shift());
    let length = Number(input.shift());
    let width = Number(input.shift());

    let coversArea = countTables * (length + 2 * 0.30) * (width + 2 * 0.30);
    let sqareCoversArea = countTables * (length / 2) * (length / 2);

    let priceUSD = ((coversArea * 7) + (sqareCoversArea * 9));
    let priceBGN = (priceUSD * 1.85);

    // Future Reminder: add the .toFixed only in the print as it tends to mess the calculations.
    console.log(`${priceUSD.toFixed(2)} USD`);
    console.log(`${priceBGN.toFixed(2)} BGN`);
}

workshop(['5', '1.00', '0.50'])
workshop(['10', '1.20', '0.65'])
