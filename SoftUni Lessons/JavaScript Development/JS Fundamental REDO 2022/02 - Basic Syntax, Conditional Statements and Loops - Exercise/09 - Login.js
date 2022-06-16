function login(array) {
    let username = array.shift();
    let tries = 0
    for (const testPassword of array) {
        if (testPassword.split("").reverse().join("") === username) {
            console.log(`User ${username} logged in.`);
            break;
        } else {
            tries++ ;
            if (tries === 4) {
                console.log(`User ${username} blocked!`);
                break;
            }
            console.log('Incorrect password. Try again.');
        }
    }
}


// login(['Acer','login','go','let me in','recA']);
login(['Acer','login','go','let me in','recA'])