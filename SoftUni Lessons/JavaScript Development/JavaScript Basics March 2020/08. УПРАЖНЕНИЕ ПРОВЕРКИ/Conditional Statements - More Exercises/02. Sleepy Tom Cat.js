function sleepyCat(input) {
    let hollydays = Number(input.shift());
    let normalDays = 365 - hollydays;

    let hollydaysPlayMinutes = hollydays * 127;
    let normalDaysPlayMinutes = normalDays * 63;

    let totalPlayTime = hollydaysPlayMinutes + normalDaysPlayMinutes;

    let differenceInminutes = Math.abs(30000 - totalPlayTime);
    let hours = ~~(differenceInminutes / 60);
    let minutes = differenceInminutes - (hours * 60);

    if (totalPlayTime > 30000) {
        console.log("Tom will run away");
        console.log(`${hours} hours and ${minutes} minutes more for play`);
    } else {
        console.log("Tom sleeps well");
        console.log(`${hours} hours and ${minutes} minutes less for play`);
    }
}

sleepyCat(["20"]);
// Expected output:
// Tom sleeps well
// 95 hours and 25 minutes less for play

sleepyCat(["113"]);
// Expected output:
// Tom will run away
// 3 hours and 47 minutes more for play
