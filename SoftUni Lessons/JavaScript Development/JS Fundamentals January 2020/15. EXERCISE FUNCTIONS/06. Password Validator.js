function passwordValidator(pass) {
    // Mask

    let checkOne = false; let checkTwo = false; let checkThree = false;

    const validateLength = ((password) => {
        // The length should be 6 - 10 characters (inclusive)
        if (password.length >= 6 && password.length <= 10) { checkOne = true; }
        else { console.log('Password must be between 6 and 10 characters') }
    })(pass);

    const checkLettersAndDigitsOnly = ((password) => {
        // It should consists only of letters and digits
        checkTwo = true;
        for (let symbol of password) {
            if (!((symbol.charCodeAt(0) >= 48 && symbol.charCodeAt(0) <= 57) ||
                (symbol.charCodeAt(0) >= 65 && symbol.charCodeAt(0) <= 90) ||
                (symbol.charCodeAt(0) >= 97 && symbol.charCodeAt(0) <= 122))) {
                checkTwo = false;
                break;
            }
        }
        if(!checkTwo) { console.log('Password must consist only of letters and digits'); }
    })(pass);

    const checkForMinimumOfTwoDigits = ((password) => {
        // It should have at least 2 digits
        let countDigits = 0;
        for (let symbol of password) {
            if (symbol.charCodeAt(0) >= 48 && symbol.charCodeAt(0) <= 57) {
                countDigits += 1;
                if (countDigits >= 2) {
                    checkThree = true;
                    break;
                }
            }
        }
        if (countDigits < 2) { console.log(`Password must have at least 2 digits`); }
    })(pass);

    if (checkOne && checkTwo && checkThree) {
        console.log(`Password is valid`)
    }
}

passwordValidator('logIn');  // Should return:
// Password must be between 6 and 10 characters
// Password must have at least 2 digits

passwordValidator('MyPass123');  // Should return:
// Password is valid

passwordValidator('Pa$s$s');  // Should return:
// Password must consist only of letters and digits
// Password must have at least 2 digits
