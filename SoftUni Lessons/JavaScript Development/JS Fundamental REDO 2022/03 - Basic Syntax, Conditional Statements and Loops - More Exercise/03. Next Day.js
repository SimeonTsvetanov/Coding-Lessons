// Write a JS function that calculates the date of the next day by given year, month, and day.
//     The input comes as three number parameters. The first element is the year, the second is the month and the third is the day.
//     The output should be returned as a result of your function.

// Input: 2016, 9, 30
// Output: 2016-10-1

function n(yyyy, mm, dd) {
    let d = new Date(yyyy, mm - 1, dd);
    d.setDate(d.getDate() + 1);
    let month = (d.getMonth() + 1).toString();
    let day = d.getDate().toString();
    let year = d.getFullYear();
    console.log([year, month, day].join('-'));
}

n(2020, 3, 24)