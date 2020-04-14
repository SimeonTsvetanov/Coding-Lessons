// (not included in final score)

function login(input) {
    // Mask
    let username = input.shift();

    let totalTrys = 0;

    for (let pass of input) {
        let reverse = pass.split('').reverse().join('');
        totalTrys += 1;
        if (reverse == username) {
            console.log(`User ${username} logged in.`);
            break;
        } else {       
            if (totalTrys == 4) {
                console.log(`User ${username} blocked!`);
                break;
            } else {
                console.log(`Incorrect password. Try again.`);
            }
        }
    }
}

login(['Acer','login','go','let me in','recA']);  // Should return:
// Incorrect password. Try again.
// Incorrect password. Try again.
// Incorrect password. Try again.
// User Acer logged in.

login(['momo','omom']);  // Should return:
// User momo logged in.