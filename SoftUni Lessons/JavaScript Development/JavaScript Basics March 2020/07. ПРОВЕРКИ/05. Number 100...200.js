// There are two ways of reading the Input for this tasks:
// This is the new way:
function numbers100To200(number) {
    // Yep I know that using lists here is pointless, BUT I wanted to try them too :D.
    outputs = ['Less than 100', 'Between 100 and 200', 'Greater than 200'];

    if (number < 100) {
        console.log(outputs[0]);
    } else if (number >= 100 && number <= 200) {
        console.log(outputs[1]);
    } else {
        console.log(outputs[2]);
    }
}

numbers100To200(95);  // Expected output: Less than 100
numbers100To200(120);  // Expected output: Between 100 and 200
numbers100To200(210);  // Expected output: Greater than 200



// -----------------------------------------------------------------------//
// This is the old way of reading the input:
function numbers100To200Old(input) {
    number = Number(input.shift());

    // Yep I know that using lists here is pointless, BUT I wanted to try them too :D.
    outputs = ['Less than 100', 'Between 100 and 200', 'Greater than 200'];

    if (number < 100) {
        console.log(outputs[0]);
    } else if (number >= 100 && number <= 200) {
        console.log(outputs[1]);
    } else {
        console.log(outputs[2]);
    }
}

numbers100To200Old(['95']);  // Expected output: Less than 100
numbers100To200Old(['120']);  // Expected output: Between 100 and 200
numbers100To200Old(['210']);  // Expected output: Greater than 200
