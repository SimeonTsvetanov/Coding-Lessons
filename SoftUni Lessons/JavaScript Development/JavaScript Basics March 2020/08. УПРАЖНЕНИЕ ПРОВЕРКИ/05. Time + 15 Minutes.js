function timePlus15Mins(input) {
    let hours = Number(input.shift());
    let minutes = Number(input.shift()) + 15;

    if (minutes > 59) {
        hours += 1;
        minutes -= 60;
    } 
    
    if (hours > 23) {
        hours -= 24;
    }
    
    if (minutes < 10) {
        console.log(`${hours}:0${minutes}`);
    } else {
        console.log(`${hours}:${minutes}`);
    }
}

timePlus15Mins(["1", "46"]);  // Expected Output: 2:01
timePlus15Mins(["0", "01"]);  // Expected Output: 0:16
timePlus15Mins(["23", "59"]);  // Expected Output: 0:14
timePlus15Mins(["11", "08"]);  // Expected Output: 11:23
timePlus15Mins(["12", "49"]);  // Expected Output: 13:04

