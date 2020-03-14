// There are two ways of reading the Input for this tasks:
// This is the new way:
function numbersOneToNine(number) {
    // Look.... I know it looks weird, but I wanted to try using objects :)
    numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine" 
    };
    if (number in numbers) {
        console.log(numbers[number]);
    } else if (false) {
        // This code is unreachable... jsut to use the esle if :D
    } else {
        console.log("number too big");
    }
}

numbersOneToNine(3); // Expected output: three
numbersOneToNine(1); // Expected output: one
numbersOneToNine(9); // Expected output: nine
numbersOneToNine(69); // Expected output: number too big




// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function numbersOneToNineOld(input) {
    number = Number(input.shift());
    // Look.... I know it looks weird, but I wanted to try using objects :)
    numbers = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine" 
    };
    if (number in numbers) {
        console.log(numbers[number]);
    }
    else if (false) {
        // This code is unreachable... jsut to use the esle if :D
    }
    else {
        console.log("number too big");
    }
}

numbersOneToNineOld([3]); // Expected output: three
numbersOneToNineOld([1]); // Expected output: one
numbersOneToNineOld([9]); // Expected output: nine
numbersOneToNineOld([69]); // Expected output: number too big
