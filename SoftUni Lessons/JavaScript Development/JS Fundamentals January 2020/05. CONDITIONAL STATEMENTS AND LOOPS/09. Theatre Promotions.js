function mask(period, age) {
    // Mask
    let price = undefined;

    if (age >= 0 && age <= 18) {
        if (period == 'Weekday') {
            price = 12;
        } else if (period == 'Weekend') {
            price = 15;
        } else if (period == "Holiday") {
            price = 5;
        }
    } else if (age > 18 && age <= 64) {
        if (period == 'Weekday') {
            price = 18;
        } else if (period == 'Weekend') {
            price = 20;
        } else if (period == "Holiday") {
            price = 12;
        }
    } else if (age > 64 && age <= 122) {
        if (period == 'Weekday') {
            price = 12;
        } else if (period == 'Weekend') {
            price = 15;
        } else if (period == "Holiday") {
            price = 10;
        }
    } else {
        price = 'Error!';
    }
    
    if (price != 'Error!') {
    console.log(`${price}$`);
    } else {
        console.log(price);
    }
}

mask('Weekday', 42);  // Should return:
// 18$

mask('Holiday', -12);  // Should return:
// Error!