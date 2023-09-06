function mask (params) {
    // MASK
    let days = params;
    let money = 0;
    let priceBitcoin = 11949.16;
    let priceGoldGr = 67.51;
    let bitcoins = 0;
    let dayOfFirstBitcoin = 0;

    days.forEach((gold , index) => {
        let day = index + 1;
        let dailyAmount = gold * priceGoldGr;

        (day % 3 === 0) ? dailyAmount *= 0.7 : 'pass';

        money += dailyAmount;

        while (money >= priceBitcoin) {
            (bitcoins === 0) ? dayOfFirstBitcoin = day : 'pass';
            bitcoins += 1;
            money -= priceBitcoin;
        }
    });

    console.log(`Bought bitcoins: ${bitcoins}`);
    (dayOfFirstBitcoin !== 0) ? console.log(`Day of the first purchased bitcoin: ${dayOfFirstBitcoin}`) : 'pass';
    console.log(`Left money: ${money.toFixed(2)} lv.`);
}

mask([100, 200, 300] );
// Bought bitcoins: 2
// Day of the first purchased bitcoin: 2
// Left money: 10531.78 lv.

mask([50, 100] );
// Bought bitcoins: 0
// Money left: 10126.50
// lv.

mask([3124.15,
504.212,
2511.124]);
// Bought bitcoins: 30
// Day of the first purchased bitcoin:
// 1
// Money left: 5144.11 lv.
