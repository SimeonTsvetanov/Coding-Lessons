// Къс линк: https://git.io/JvjRq

function dishwasher(params) {
    let detergent = 750 * Number(params.shift());
    let dishes = 0;
    let pots = 0

    let timesInHell = 0;
    while('You wash them dirty bit**s') {
        let plates = params.shift();
        if (plates == 'End') {break;}
        
        timesInHell += 1
        plates = Number(plates);
        if (timesInHell % 3 == 0) {detergent -= (plates * 15); pots += plates;}
        else {detergent -=plates * 5; dishes += plates}
        
        if (detergent < 0) {break;}
    }

    if (detergent >= 0) {
        console.log(`Detergent was enough!`);
        console.log(`${dishes} dishes and ${pots} pots were washed.`);
        console.log(`Leftover detergent ${detergent} ml.`);
    } else {
        console.log(`Not enough detergent, ${Math.abs(detergent)} ml. more necessary!`);
    }
}

dishwasher([2, 53, 65, 55, 'End']);  // Expected Output:
// Detergent was enough!
// 118 dishes and 55 pots were washed.
// Leftover detergent 85 ml.


dishwasher([1, 10, 15, 10, 12, 13, 30]);  // Expected Output:
// Not enough detergent, 100 ml. more necessary!
