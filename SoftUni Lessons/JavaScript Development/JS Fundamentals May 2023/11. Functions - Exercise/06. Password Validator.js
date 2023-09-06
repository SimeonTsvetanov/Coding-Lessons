function mask (password) {
    // MASK

    let valid = true;

    if (password.length < 6 || password.length > 10) {
        console.log(`Password must be between 6 and 10 characters`);
        valid = false;
    }

    if (!(/^[A-Za-z0-9]*$/.test(password))) {
        console.log('Password must consist only of letters and digits');
        valid = false;
    }

    if (!(/\(|\)|\d{2}/.test(password))) {
        console.log(`Password must have at least 2 digits`);
        valid = false;
    }

    (valid) ? console.log(`Password is valid`) : 'pass';
}

mask('logIn');
//

console.log('-------------------------------------');

mask('MyPass123');
// Password is valid
