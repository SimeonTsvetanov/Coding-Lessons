function daysOfTheWeek(day) {
    // Mask
    day = Number(day);
    let days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ];
    if (day >= 1 && day <= 7) {
        console.log(days[day - 1]);
    } else {
        console.log(`Invalid day!`);
    }
}

daysOfTheWeek(3);  // Should return: Wednesday

daysOfTheWeek(11);  // Should return: Invalid day!