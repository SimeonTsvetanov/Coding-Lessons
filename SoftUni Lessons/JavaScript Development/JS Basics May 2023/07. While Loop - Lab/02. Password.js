function passwords(params) {
    let name = params.shift();
    let password = params.shift();

    while ('I say SO!!!') {
        let checkPass = params.shift();
        if (password === checkPass) {
            console.log(`Welcome ${name}!`);
            break;
        }
    }
}

passwords(["Nakov",
"1234",
"Pass",
"1324",
"1234"]);

// Welcome Nakov!
