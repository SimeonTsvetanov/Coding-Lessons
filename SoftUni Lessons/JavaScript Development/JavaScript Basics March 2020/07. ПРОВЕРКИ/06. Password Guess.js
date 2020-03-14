// There are two ways of reading the Input for this tasks:
// This is the new way:
function passwordGuess(guessPassword) {
    let password = "s3cr3t!P@ssw0rd";
    
    if (password === guessPassword){
        console.log("Welcome");
    } else {
        console.log("Wrong password!");
    }
}

passwordGuess('qwerty');  // Expected output: Wrong password!
passwordGuess('s3cr3t!P@ssw0rd');  // Expected output: Welcome
passwordGuess('s3cr3t!p@ss');  // Expected output: Wrong password!



// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function passwordGuessOld(input) {
    let password = "s3cr3t!P@ssw0rd";
    let guessPassword = input.shift();
    
    if (password === guessPassword){
        console.log("Welcome");
    } else {
        console.log("Wrong password!");
    }
}

passwordGuessOld(['qwerty']);  // Expected output: Wrong password!
passwordGuessOld(['s3cr3t!P@ssw0rd']);  // Expected output: Welcome
passwordGuessOld(['s3cr3t!p@ss']);  // Expected output: Wrong password!
