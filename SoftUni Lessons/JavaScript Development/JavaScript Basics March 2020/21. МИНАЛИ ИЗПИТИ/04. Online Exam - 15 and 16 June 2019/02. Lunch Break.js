function lunchBreak(params) {
    let name = params.shift();
    let episodeTime = Number(params.shift());
    let breakTime = Number(params.shift());

    let time = breakTime - (breakTime * (1 / 8)) - (breakTime * (1 / 4));
    let remainder = Math.ceil(Math.abs(episodeTime - time));

    if (time >= episodeTime) {
        console.log(`You have enough time to watch ${name} and left with ${remainder} minutes free time.`);
    } else {
        console.log(`You don't have enough time to watch ${name}, you need ${remainder} more minutes.`);
    }
}


lunchBreak(['Game of Thrones', '60', '96']);  // Expected Output:
// You have enough time to watch Game of Thrones and left with 0 minutes free time.


lunchBreak(['Teen Wolf', '48', '60']);  // Expected Output:
// You don't have enough time to watch Teen Wolf, you need 11 more minutes.

