function mining(amounts) {
    let gold = 67.51;
    let bitCoin = 11949.16;
    let money = 0;
    let firstBitCoinDay = undefined;
    let bitCoins = 0

    amounts.forEach((amount, index) => {
        let day = index + 1;

        let dailyMoney = amount * gold;
        day % 3 === 0 ? dailyMoney *= 0.7 : 'pass without P';

        money += dailyMoney;
        if (money >= bitCoin) {
            while (money >= bitCoin) {
                bitCoins += 1;
                money -= bitCoin;
                !firstBitCoinDay ? firstBitCoinDay = day : 'not virgin';
            }
        }
    });

    console.log(`Bought bitcoins: ${bitCoins}`);
    firstBitCoinDay ? console.log( `Day of the first purchased bitcoin: ${firstBitCoinDay}`) : 'pass';
    console.log(`Left money: ${money.toFixed(2)} lv.`);
}

mining([100, 200, 300]);
mining([50, 100]);
mining([3124.15, 504.212, 2511.124]);
