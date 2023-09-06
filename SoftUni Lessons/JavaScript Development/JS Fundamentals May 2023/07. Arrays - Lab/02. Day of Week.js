/**
 * Write a program, which receives a number and prints
 * the corresponding name of the day of the week (in English).
 * If the number is NOT a valid day, print: "Invalid day!".
 * @param day {Number} The day of the week in number.
 * @return {String} The day of the week in English or Invalid day!.
 */
function mask (day) {
    // MASK
    const days = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday' };
    (day in days) ? console.log(days[day]) : console.log('Invalid day!');
}

mask(3);
// Wednesday

mask(11);
// Invalid day!
