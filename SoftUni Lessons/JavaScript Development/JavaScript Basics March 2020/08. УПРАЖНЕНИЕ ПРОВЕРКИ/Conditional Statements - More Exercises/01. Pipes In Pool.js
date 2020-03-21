function pipesInPool(...input) {
    let volume = Number(input.shift());
    let debitP1 = Number(input.shift());
    let debitP2 = Number(input.shift());
    let hours = Number(input.shift());

    let fillingP1 = debitP1 * hours;
    let fillingP2 = debitP2 * hours;

    if ((fillingP1 + fillingP2) > volume) {  
        // RIP 15 minutes lost for one f****** "="
        
        // So we have the pool filled :)
        console.log(`For ${hours} hours the pool overflows with ${((fillingP1 + fillingP2) - volume)} liters.`);
    } else {
        // The pool remained unfilled :D (as my childhood wishes ;(  ))
        let percentP1 = ((fillingP1 / (fillingP1 + fillingP2)) * 100).toFixed(2);
        let percentP2 = (fillingP2 / (fillingP1 + fillingP2) * 100).toFixed(2);
        let percentFilled = ((fillingP1 + fillingP2) / volume * 100).toFixed(2);
        console.log(`The pool is ${percentFilled}% full. Pipe 1: ${percentP1}%. Pipe 2: ${percentP2}%.`);
    }
}

pipesInPool(["1000", "100", "120", "3"]);  
// Expected Output: The pool is 66.00% full. Pipe 1: 45.45%. Pipe 2: 54.55%.

pipesInPool(["100", "100", "100", "2.5"]);
// Expected Output: For 2.50 hours the pool overflows with 400.00 liters.
