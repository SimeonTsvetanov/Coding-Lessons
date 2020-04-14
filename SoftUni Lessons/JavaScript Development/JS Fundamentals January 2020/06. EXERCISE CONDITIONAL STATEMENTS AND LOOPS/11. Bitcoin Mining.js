// (not included in final score)

function bitcoinMining(input) {
    // Mask
    let goldValue = 67.51;
    let bitcoinValue = 11949.16;

    let bitcoinCount = 0;

    let firstDay;

    let totalMoney = 0;

    for (let i = 1; i <= input.length; i++) {
        let goldMined = input[i - 1];

        if (i % 3 == 0) {
            goldMined *= 0.7;
            totalMoney += goldMined * goldValue;
        } else {
            totalMoney += goldMined * goldValue;
        }

        if (totalMoney >= bitcoinValue) {
            if (firstDay == undefined) {
                firstDay = i;
            }
            bitcoinCount += parseInt(totalMoney / bitcoinValue);
            totalMoney -= parseInt(totalMoney / bitcoinValue) * bitcoinValue;
        }
    }

    console.log(`Bought bitcoins: ${bitcoinCount}`);
    
    if (firstDay != undefined) {
        console.log(`Day of the first purchased bitcoin: ${firstDay}`);
    }
    
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}

bitcoinMining([100,200,300]);  // Should return:
// Bought bitcoins: 2
// Day of the first purchased bitcoin: 2
// Left money: 10531.78 lv.

bitcoinMining([50, 100]);  // Should return:
// Bought bitcoins: 0
// Money left: 10126.50 lv.
