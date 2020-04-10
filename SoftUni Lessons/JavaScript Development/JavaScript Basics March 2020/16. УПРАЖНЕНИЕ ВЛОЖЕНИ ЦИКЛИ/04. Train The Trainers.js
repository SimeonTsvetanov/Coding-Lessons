function trainTheTrainers(input) {
    // Mask
    let judges = Number(input.shift());
    
    let total = 0;
    let times = 0;

    while('command is Finish') {
        let presentation = input.shift();
        if (presentation == "Finish") {break;}

        let scores = 0;
        for (let judge = 1; judge <= judges; judge++) {
            let score = Number(input.shift());
            total += score;
            scores += score;
            times += 1;
        }
        console.log(`${presentation} - ${(scores / judges).toFixed(2)}.`);
    }

    console.log(`Student's final assessment is ${(total / times).toFixed(2)}.`);
}


trainTheTrainers([2, 'While-Loop', 6.00, 5.50,'For-Loop', 5.84, 5.66, 'Finish']);  // Should return:
// While-Loop - 5.75.
// For-Loop - 5.75.
// Student's final assessment is 5.75.

trainTheTrainers([3, 'Arrays',4.53, 5.23, 5.00, 'Lists',5.83, 6.00, 5.42, 'Finish']);  // Should return:
// Arrays - 4.92.
// Lists - 5.75.
// Student's final assessment is 5.34.
