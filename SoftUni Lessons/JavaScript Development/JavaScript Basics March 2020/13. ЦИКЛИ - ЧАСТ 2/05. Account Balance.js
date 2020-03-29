function accountBalance(params) {
    let balance = 0;  // Sad but true :D

    let times = Number(params.shift());

    // FYI: I can solve it with while but just to play around I've used FOR.
    for (let time = 1; time <= times; time++) {
        let deposit = Number(params.shift());
        if (deposit < 0) {
            console.log(`Invalid operation!`);            
            break;
        }
        console.log(`Increase: ${deposit.toFixed(2)}`)
        balance += deposit
    }

    console.log(`Total: ${balance.toFixed(2)}`);
}

accountBalance([3, 5.51, 69.42, 100]);  // Expected Output:
// Increase: 5.51
// Increase: 69.42
// Increase: 100
// Total: 174.93
