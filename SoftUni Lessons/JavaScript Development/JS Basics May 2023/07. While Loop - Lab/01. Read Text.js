function readText(params) {
    while ('I say so!!!') {
        let text = params.shift();
        if (text === "Stop") {
            break
        } else {
            console.log(text);
        }
    }
}

readText(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);

// Nakov
// SoftUni
// Sofia
// Bulgaria
// SomeText
