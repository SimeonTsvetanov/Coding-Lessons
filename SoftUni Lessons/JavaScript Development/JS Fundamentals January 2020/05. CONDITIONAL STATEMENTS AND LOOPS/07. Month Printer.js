function monthPrinter(month) {
    // Mask
    let months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"};
    if (month in months) {
        console.log(months[month]);
    } else {
        console.log("Error!");
    }
}

monthPrinter(2);  // Should return:
// February

monthPrinter(13);  // Should return:
// Error!