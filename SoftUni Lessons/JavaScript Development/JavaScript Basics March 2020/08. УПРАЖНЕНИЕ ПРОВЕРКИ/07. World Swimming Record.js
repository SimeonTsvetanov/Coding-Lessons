function worldSwimmingRecord(input) {
    let record = Number(input.shift());
    let meters = Number(input.shift());
    let timeFor1M = Number(input.shift());

    let totalTime = (meters * timeFor1M) + (Math.floor(meters / 15)) * 12.5;

    if (totalTime < record) {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`);
    } else {
        console.log(`No, he failed! He was ${(totalTime - record).toFixed(2)} seconds slower.`);
    }
}

worldSwimmingRecord(["10464", "1500", "20"]);
// Expected output:
// No, he failed! He was 20786.00 seconds slower.

worldSwimmingRecord(["55555.67", "3017", "5.03"]);
// Expected output:
// Yes, he succeeded! The new world record is 17688.01 seconds.
