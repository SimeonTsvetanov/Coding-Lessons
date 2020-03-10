function speedInfo(input) {
    let speed = Number(input.shift());
    
    if (speed <= 10) {
        console.log("slow");
    } else if (speed <= 50) {
        console.log("average");
    } else if (speed <= 150) {
        console.log("fast");
    } else if (speed <= 1000) {
        console.log("ultra fast");
    } else if (speed > 1000) {
        console.log("extremely fast");
    }
}

speedInfo([8]); // Expected Output: slow
speedInfo([49.5]); // Expected Output: average
speedInfo([126]); // Expected Output: fast
speedInfo([160]); // Expected Output: ultra fast
speedInfo([3500]); // Expected Output: extremely fast
