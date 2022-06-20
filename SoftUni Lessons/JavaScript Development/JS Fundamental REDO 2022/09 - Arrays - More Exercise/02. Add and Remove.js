function addAndRemove (commands) {
    // MasK
    let result = [];  // We will keep the result here!
    let n = 1;  // Set the number with starting value 1
    for (const command of commands) {
        command === 'add' ? result.push(n) : result.pop();  // Add the number or remove the last one!
        n++;  // Increment the value of N
    }

    result.length > 0 ? console.log(result.join(' ')) : console.log('Empty');  // Print the Result
}

addAndRemove(['add', 'add', 'add', 'add']);  // 1 2 3 4
addAndRemove(['add', 'add', 'remove', 'add', 'add']);  // 1 4 5