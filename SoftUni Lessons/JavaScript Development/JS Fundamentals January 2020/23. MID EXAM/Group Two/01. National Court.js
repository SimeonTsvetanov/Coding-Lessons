function nationalCourt(input) {
    // Mask
    let [employeeOne, employeeTwo, employeeThree, countPeople] = input.map(Number);

    let pph = employeeOne + employeeTwo + employeeThree; // People Per Hour
    let timeNeeded = 0;
    let days = 0;

    while (countPeople > 0) {
        countPeople -= pph;
        timeNeeded++;
        if (timeNeeded % 4 === 0 && timeNeeded !== 0) {
            timeNeeded++;
            if (timeNeeded >= 24) {
                days++;
                timeNeeded -= 24;
            }
        }
    }
    console.log(`Time needed: ${days * 24 + timeNeeded}h.`);
}

nationalCourt([ '5', '6', '4', '20' ]);
// Should return: Time needed: 2h.

nationalCourt([ '1', '2', '3', '45' ]);
// Should return: Time needed: 10h.
