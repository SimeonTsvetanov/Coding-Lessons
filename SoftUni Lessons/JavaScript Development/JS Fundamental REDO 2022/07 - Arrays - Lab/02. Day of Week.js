function dayOfWeek (day) {
    // MasK
    let days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'};
    days.hasOwnProperty(day) ? console.log(days[day]) : console.log('Invalid day!');
}

dayOfWeek(3);