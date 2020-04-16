function centuriesToMinutes(centuries) {
    // Mask
    let years = centuries * 100;
    let days = Math.floor(years * 365.2422);
    let hours = days * 24;
    let minutes = hours * 60;

    console.log(`${centuries} centuries = ${years} years = ${days} days = ${hours} hours = ${minutes} minutes`);
}

centuriesToMinutes(1);  // Should return:
// 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes

centuriesToMinutes(5);  // Should return:
// 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes
