function solution(params) {
    // MasK
    let tickets = { 'student': 0, 'standard': 0, 'kid': 0 };
    
    while('Finish') {
        let movie = params.shift();
        if (movie === 'Finish') { break; }
        let seats = Number(params.shift());
        let takenSeats = 0;
        while(seats !== takenSeats) {
            let ticket = params.shift();
            if (ticket === 'End') { break; }
            takenSeats += 1;
            tickets[ticket] += 1;
        }
        console.log(`${movie} - ${(takenSeats / seats * 100).toFixed(2)}% full.`);
    }

    let totalTickets = Object.values(tickets).reduce((a, b) => a + b, 0);
    
    console.log(`Total tickets: ${totalTickets}`);
    console.log(`${(tickets['student'] / totalTickets * 100).toFixed(2)}% student tickets.`);
    console.log(`${(tickets['standard'] / totalTickets * 100).toFixed(2)}% standard tickets.`);
    console.log(`${(tickets['kid'] / totalTickets * 100).toFixed(2)}% kids tickets.`);
}

solution(["Taxi",
"10",
"standard",
"kid",
"student",
"student",
"standard",
"standard",
"End",
"Scary Movie",
"6",
"student",
"student",
"student",
"student",
"student",
"student",
"Finish"]);

// Taxi - 60.00% full.
// Scary Movie - 100.00% full.
// Total tickets: 12
// 66.67% student tickets.
// 25.00% standard tickets.
// 8.33% kids tickets.

console.log('********************************');

solution(["The Matrix",
"20",
"student",
"standard",
"kid",
"kid",
"student",
"student",
"standard",
"student",
"End",
"The Green Mile",
"17",
"student",
"standard",
"standard",
"student",
"standard",
"student",
"End",
"Amadeus",
"3",
"standard",
"standard",
"standard",
"Finish"]);

// The Matrix - 40.00% full.
// The Green Mile - 35.29% full.
// Amadeus - 100.00% full.
// Total tickets: 17
// 41.18% student tickets.
// 47.06% standard tickets.
// 11.76% kids tickets.
