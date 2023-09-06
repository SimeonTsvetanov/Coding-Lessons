function mask (params) {
    // MASK
    const user = params.shift()
    const pass = user.split("").reverse().join("");

    let tries = 0;

    for (const tryPass of params) {
        if (tryPass === pass) {
            console.log(`User ${user} logged in.`);
            break;
        } else {
            tries += 1;
            if (tries == 4) {
                console.log(`User ${user} blocked!`);
                break
            }
            console.log(`Incorrect password. Try again.`);
        }
    }
}

mask(['Acer','login','go','let me in','recA']);
// Incorrect password. Try again.
// Incorrect password. Try again.
// Incorrect password. Try again.
// User Acer logged in.

mask(['momo','omom']);
// User momo logged in.

mask(['sunny','rainy','cloudy','sunny','not sunny']);
// Incorrect password. Try again.
// Incorrect password. Try again.
// Incorrect password. Try again.
// User sunny blocked!
