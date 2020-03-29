function password(params) {
    let name = params.shift();
    let pass = params.shift();

    guess = params.shift();
    while (guess != pass) {
        guess = params.shift();
    }

    console.log(`Welcome ${name}!`);
}

password(['Nakov', '1234','pass', '1324', '1234']);
// Expected Output: Welcome Nakov!