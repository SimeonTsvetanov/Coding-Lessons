function passwordValidator (pass) {
    // MasK
    let a, b ,c;
    if (pass.length >= 6 && pass.length <= 10) {
        a = true
    } else {
        console.log(`Password must be between 6 and 10 characters`);
    }

    if (/^[A-Za-z\d]*$/.test(pass)) {
        b = true;
    } else {
        console.log("Password must consist only of letters and digits");
    }

    if (/\(|\)|\d{2}/.test(pass)) {
        c = true;
    } else {
        console.log('Password must have at least 2 digits');
    }


    if (a && b && c) {
        console.log('Password is valid');
    }
}

passwordValidator('logIn');
// Password must be between 6 and 10 characters
// Password must have at least 2 digits

passwordValidator('MyPass123');
// Password is valid