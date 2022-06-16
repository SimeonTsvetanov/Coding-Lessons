function centuriesToMinutes(centuries) {
    // Mask
    let years = centuries * 100;
    let days = Math.floor(years * 365.2422);
    let hours = days * 24;
    let minutes = hours * 60;

    console.log(`${centuries} centuries = ${years} years = ${days} days = ${hours} hours = ${minutes} minutes`);
}
