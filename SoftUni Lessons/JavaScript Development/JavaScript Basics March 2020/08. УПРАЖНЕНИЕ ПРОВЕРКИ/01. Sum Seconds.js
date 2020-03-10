function sumSeconds(input) {
    let totalTime = Number(input.shift()) + Number(input.shift()) + Number(input.shift());
    
    let minutes = ~~(totalTime / 60);
    let seconds = totalTime % 60;
    
    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
    } else {
        console.log(`${minutes}:${seconds}`);
    }
}

sumSeconds(["35", "45", "44"]);  // Expexted output: 2:04
sumSeconds(["22", "7", "34"]);  // Expexted output: 1:03
sumSeconds(["50", "50", "49"]);  // Expexted output: 2:29
sumSeconds(["14", "12", "10"]);  // Expexted output: 0:36
