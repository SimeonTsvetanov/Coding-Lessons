function leapYear(year) {
    // Mask
    
    // let leap = 'no';

    // if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    //     leap = 'yes';
    // }

    // console.log(leap);

    console.log(year % 4 == 0 && year % 100 != 0 || year % 400 == 0 ? 'yes' : 'no');
}

leapYear(1984);  // Should return: yes

leapYear(2003);  // Should return: no

leapYear(4);  // Should return: yes
