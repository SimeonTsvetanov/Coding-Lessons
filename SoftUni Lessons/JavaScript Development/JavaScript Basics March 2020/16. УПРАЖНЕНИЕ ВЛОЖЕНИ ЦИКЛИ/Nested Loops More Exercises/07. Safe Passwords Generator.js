function safePasswordsGenerator(input) {
    // Mask
    // 'A'.charCodeAt(0)        --> Will return the digit 65
    // String.fromCharCode(65)  --> Will return the letter A

    let a = Number(input.shift());
    let b = Number(input.shift());
    let count = Number(input.shift());

    let A = 35;
    let B = 64;

    let result = '';

    for (let x = 1; x <= a; x += 1) {
        if (count == 0) {break;}

        for (let y = 1; y <= b; y += 1) {
            if (count == 0) {break;}
            
            if (A > 55) {A = 35;}
            if (B > 96) {B = 64;}

            result += `${String.fromCharCode(A)}${String.fromCharCode(B)}${x}${y}${String.fromCharCode(B)}${String.fromCharCode(A)}|`;

            A += 1;
            B += 1;
            count -= 1;
        }
    }

    console.log(result);
}



safePasswordsGenerator([2, 3, 10]);  // Should return:
// #@11@#|$A12A$|%B13B%|&C21C&|'D22D'|(E23E(|

safePasswordsGenerator([20, 50, 10]);  // Should return:
// #@11@#|$A12A$|%B13B%|&C14C&|'D15D'|(E16E(|)F17F)|*G18G*|+H19H+|,I110I,|