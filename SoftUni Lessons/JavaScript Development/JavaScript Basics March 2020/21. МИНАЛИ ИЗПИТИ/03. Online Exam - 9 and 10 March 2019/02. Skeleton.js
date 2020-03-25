function skeleton(params) {
    let minutesRecord = Number(params.shift());
    let secondsRecord = Number(params.shift());
    let length = Number(params.shift());
    let secondsFor100meters = Number(params.shift());

    let record = (minutesRecord * 60) + secondsRecord;
    let timeCheat = (length / 120) * 2.5;
    let marinTime = (length / 100) * secondsFor100meters - timeCheat;

    if (marinTime <= record) {
        console.log(`Marin Bangiev won an Olympic quota!`);
        console.log(`His time is ${marinTime.toFixed(3)}.`);
    } else {
        console.log(`No, Marin failed! He was ${(marinTime - record).toFixed(3)} second slower.`);
    }
}


skeleton(['2', '12', '1200', '10']);  // Expected Output:
// Marin Bangiev won an Olympic quota!
// His time is 95.000.

skeleton(['1', '20', '1546', '12']);  // Expected Output:
// No, Marin failed! He was 73.312 second slower.
