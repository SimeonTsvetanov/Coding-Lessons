function biscuitsFactory(input) {
    // Mask
    let [biscuitsPerDay, workers, competition] = input.map(Number);
    let total = 0;

    function percentage(part, whole) {
        return `${Math.abs((100 * part / whole) - 100).toFixed(2)}`;
    }

    for (let day = 1; day <= 30; day += 1) {
        let biscuits = biscuitsPerDay * workers;
        day % 3 === 0 ? biscuits *= 0.75 : 'pass';
        total += Math.floor(biscuits);
    }


    console.log(`You have produced ${total} biscuits for the past month.`);
    if (total > competition) {
        console.log(`You produce ${percentage(total, competition)} percent more biscuits.`);
    } else {
        console.log(`You produce ${percentage(total, competition)} percent less biscuits.`);
    }
}

biscuitsFactory([78, 8, 16000]);  // Should return:
// You have produced 17160 biscuits for the past month.
// You produce 7.25 percent more biscuits.


biscuitsFactory([65, 12, 26000]);  // Should return:
// You have produced 21450 biscuits for the past month.
// You produce 17.50 percent less biscuits.
