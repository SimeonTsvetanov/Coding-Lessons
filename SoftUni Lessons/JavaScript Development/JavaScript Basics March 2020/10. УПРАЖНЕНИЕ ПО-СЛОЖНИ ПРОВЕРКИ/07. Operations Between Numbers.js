function OperationsBetweenNumbers(...input) {
    let n1 = Number(input.shift());
    let n2 = Number(input.shift());
    let delitel = input.shift();

    let evenOrOdd = '';
    let result = undefined;

    switch (delitel) {
        case "+":
            result = n1 + n2;
            if (result % 2 == 0) {
                evenOrOdd = "even";
            } else{
                evenOrOdd = "odd";
            }
            console.log(`${n1} ${delitel} ${n2} = ${result} - ${evenOrOdd}`);
            break;
        case "-":
            result = n1 - n2;
            if (result % 2 == 0) {
                evenOrOdd = "even";
            } else{
                evenOrOdd = "odd";
            }
            console.log(`${n1} ${delitel} ${n2} = ${result} - ${evenOrOdd}`);
            break;
        case "*":
            result = n1 * n2;
            if (result % 2 == 0) {
                evenOrOdd = "even";
            } else{
                evenOrOdd = "odd";
            }
            console.log(`${n1} ${delitel} ${n2} = ${result} - ${evenOrOdd}`);
            break;
        case "/":
            if (n2 == 0) {
                console.log(`Cannot divide ${n1} by zero`);
            } else {
                console.log(`${n1} ${delitel} ${n2} = ${(n1 / n2).toFixed(2)}`);
            }
            break;
        case "%":
            if (n2 == 0) {
                console.log(`Cannot divide ${n1} by zero`);
            } else {
                console.log(`${n1} ${delitel} ${n2} = ${(n1 % n2)}`);
            }
            break;
        default:
            break;
    }
}

OperationsBetweenNumbers(['10', '12', '+']);
// Expected Output: 10 + 12 = 22 - even

OperationsBetweenNumbers(['10', '1', '-']);
// Expected Output: 10 – 1 = 9 - odd

OperationsBetweenNumbers(['123', '12', '/']);
// Expected Output: 123 / 12 = 10.25

OperationsBetweenNumbers(['10', '3', '%']);
// Expected Output: 10 % 3 = 1

OperationsBetweenNumbers(['112', '0', '/']);
// Expected Output: Cannot divide 112 by zero

OperationsBetweenNumbers(['10', '0', '%']);
// Expected Output: Cannot divide 112 by zero