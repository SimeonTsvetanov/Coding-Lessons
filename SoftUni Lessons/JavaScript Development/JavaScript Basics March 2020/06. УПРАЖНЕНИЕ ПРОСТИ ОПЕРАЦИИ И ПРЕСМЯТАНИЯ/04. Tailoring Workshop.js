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
