function passwordGuess(input) {
    let password = "s3cr3t!P@ssw0rd";
    let guessPassword = input.shift();
    
    if (password === guessPassword){
        console.log("Welcome");
    }
    else {
        console.log("Wrong password!");
    }
}

passwordGuess(['qwerty']);  // Expected output: Wrong password!
passwordGuess(['s3cr3t!P@ssw0rd']);  // Expected output: Welcome
passwordGuess(['s3cr3t!p@ss']);  // Expected output: Wrong password!
