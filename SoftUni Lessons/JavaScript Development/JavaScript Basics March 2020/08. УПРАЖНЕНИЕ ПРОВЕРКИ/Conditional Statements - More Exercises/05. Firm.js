function firm(input) {
    let neededHours = Number(input.shift());
    let daysAvaiable = Number(input.shift());
    let extraWorkers = Number(input.shift());  // That poor bastards!!!

    let avaiableHours = Math.floor(((daysAvaiable * 0.9) * 8) + (extraWorkers * (2 * daysAvaiable)));
 
    if (avaiableHours >= neededHours) {
        console.log(`Yes!${avaiableHours - neededHours} hours left.`);
    } else {
        console.log(`Not enough time!${neededHours - avaiableHours} hours needed.`)
    }
}

firm(['90', '7', '3']);  // Expected Output: Yes!2 hours left.
firm(['99', '3', '1']);  // Expected Output: Not enough time!72 hours needed.
firm(['50', '5', '2']);  // Expected Output: Yes!6 hours left.
