function meetings (data) {
    // MasK
    let scheduled = {};

    data.forEach(meeting => {
        let [day, name] = meeting.split(' ');

        if (scheduled.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            scheduled[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    });

    for (const [day, name] of Object.entries(scheduled)) {
        console.log(`${day} -> ${name}`);
    }
}

meetings(['Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim']
);

// Scheduled for Monday
// Scheduled for Wednesday
// Conflict on Monday!
// Scheduled for Friday
// Monday -> Peter
// Wednesday -> Bill
// Friday -> Tim
