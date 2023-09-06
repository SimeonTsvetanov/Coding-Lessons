function mask (params) {
    // MASK
    let schedule = {}

    params.forEach(param => {
        [day, name] = param.split(' ');
        if (day in schedule) {
            console.log(`Conflict on ${day}!`);
        } else {
            schedule[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    });

    for (const [day, name] of Object.entries(schedule)) {
        console.log(`${day} -> ${name}`);
    }
}

mask(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']);
// Scheduled for Monday
// Scheduled for Wednesday
// Conflict on Monday!
// Scheduled for Friday
// Monday -> Peter
// Wednesday -> Bill
// Friday -> Tim

console.log('-------------------------------------');

mask(['Friday Bob',
'Saturday Ted',
'Monday Bill',
'Monday John',
'Wednesday George']);
// Scheduled for Friday
// Scheduled for Saturday
// Scheduled for Monday
// Conflict on Monday!
// Scheduled for Wednesday
// Friday -> Bob
// Saturday -> Ted
// Monday -> Bill
// Wednesday -> George
