function perfectNumber(number) {
    // Mask
    let temp = 0;
    for(let i = 1; i <= number / 2; i++) {
        if (number % i === 0) {
            temp += i;
        }
    }

    if(temp === number && temp !== 0) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }
}

perfectNumber(6);  // Should Return  We have a perfect number!
perfectNumber(28);  // Should Return  We have a perfect number!
perfectNumber(1236498);  // It's not so perfect.
