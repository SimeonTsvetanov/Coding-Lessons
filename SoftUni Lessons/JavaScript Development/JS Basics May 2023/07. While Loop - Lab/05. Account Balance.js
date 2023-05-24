function solution(params) {
    // MasK
    let total = 0;

    while ('i say so!') {
        command = params.shift();
        if (command === 'NoMoreMoney') {
            break;
        }
        amount = Number(command)
        if (amount < 0) {
            console.log('Invalid operation!');
            break;
        }
        console.log(`Increase: ${amount.toFixed(2)}`);
        total += amount;
    }

    console.log(`Total: ${total.toFixed(2)}`);
}

solution(["5.51", 
"69.42",
"100",
"NoMoreMoney"]);

// Increase: 5.51
// Increase: 69.42
// Increase: 100.00
// Total: 174.93

console.log('********************************');

solution(["120",
"45.55",
"-150"]);

// Increase: 120.00
// Increase: 45.55
// Invalid operation!
// Total: 165.55
