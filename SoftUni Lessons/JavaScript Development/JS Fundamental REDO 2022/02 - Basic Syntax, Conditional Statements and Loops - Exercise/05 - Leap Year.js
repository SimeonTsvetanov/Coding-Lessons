function leap_year(year) {
    (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0) ? console.log('yes') : console.log('no');
}

leap_year(1984);
leap_year(2003);
leap_year(4);
