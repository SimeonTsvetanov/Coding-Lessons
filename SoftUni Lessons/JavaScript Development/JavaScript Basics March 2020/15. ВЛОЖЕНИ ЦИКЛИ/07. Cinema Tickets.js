function cinemaTickets(input) {
    // Mask
    
    let student = 0;
    let standard = 0;
    let kid = 0;

    while('command is Finishito') {
        let name = input.shift();
        if (name == 'Finish') {break;}

        let free = Number(input.shift());
        let taken = 0;

        while ('command is Endito or NO more space') {
            let ticket = input.shift();
            if (ticket == "End") {
                break;
            }

            if (ticket == 'student') {student += 1;}
            else if (ticket == 'standard') {standard += 1;}
            else if (ticket == 'kid') {kid += 1;}

            taken += 1;
            if (free == taken) {break;}  // No more space.
        }

        console.log(`${name} - ${(taken / free * 100).toFixed(2)}% full.`)
    }

    let total = standard + student + kid
    console.log(`Total tickets: ${total}`);
    console.log(`${(student / total * 100).toFixed(2)}% student tickets.`);
    console.log(`${(standard / total * 100).toFixed(2)}% standard tickets.`);
    console.log(`${(kid / total * 100).toFixed(2)}% kids tickets.`);
}

cinemaTickets(['Taxi', 10, 'standard','kid', 'student', 'student', 'standard', 'standard', 'End', 'Scary Movie', 6, 'student', 'student', 'student', 'student', 'student', 'student', 'Finish']);  
// Should return:
// Taxi - 60.00% full.
// Scary Movie - 100.00% full.
// Total tickets: 12
// 66.67% student tickets.
// 25.00% standard tickets.
// 8.33% kids tickets.

cinemaTickets(['The Matrix', 20, 'student', 'standard', 'kid', 'kid', 'student', 'student', 'standard', 'student', 'End', 'The Green Mile', 17, 'student', 'standard', 'standard', 'student', 'standard', 'student', 'End', 'Amadeus', 3, 'standard', 'standard', 'standard', 'Finish']);  
// Should return:
// The Matrix - 40.00% full.
// The Green Mile - 35.29% full.
// Amadeus - 100.00% full.
// Total tickets: 17
// 41.18% student tickets.
// 47.06% standard tickets.
// 11.76% kids tickets.
