function mountainRun(input) {
    // Mask
    let record = Number(input.shift());
    let distance = Number(input.shift());
    let timePerMeter = Number(input.shift());

    let time = (distance * timePerMeter) + (Math.floor(distance / 50) * 30);

    if (time < record) {
        console.log(`Yes! The new record is ${time.toFixed(2)} seconds.`);
    } else {
        console.log(`No! He was ${(time - record).toFixed(2)} seconds slower.`);
    }
}

mountainRun([10164, 1400, 25]);  // Should return:
// No! He was 25676.00 seconds slower.

mountainRun([5554.36, 1340, 3.23]);  // Should return:
// Yes! The new record is 5108.20 seconds.
