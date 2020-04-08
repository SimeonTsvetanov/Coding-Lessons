function darts(input) {
    // Mask
    let player = input.shift();
    let total = 301;
    let shots = 0;
    let retired = 0;

    while ('Stuped motherf***er wins or retires') {
        let zone = input.shift();
        
        if (zone == "Retire") {
            console.log(`${player} retired after ${retired} unsuccessful shots.`)
            break;
        }
        
        let points = Number(input.shift());
        
        if (zone == "Double") {points = points * 2;}
        if (zone == "Triple") {points = points * 3;}

        if (total - points < 0) {
            retired += 1
        } else if (total - points == 0) {
            // Win Win Win...
            total -= points
            shots += 1
            console.log(`${player} won the leg with ${shots} shots.`)
            break;
        } else {
            total -= points;
            shots += 1
        }
    }
}

darts(['Michael van Gerwen', 'Triple', 20, 'Triple', 19, 'Double', 10, 'Single', 3, 'Single', 1, 'Triple', 20, 'Triple', 20, 'Double', 20]);  
// Should return:
// Michael van Gerwen won the leg with 8 shots.

darts(['Stephen Bunting', 'Triple', 20, 'Triple', 20, 'Triple', 20, 'Triple', 20, 'Triple', 20, 'Triple', 20, 'Double', 7, 'Single', 12, 'Double', 1, 'Single', 1]);  
// Should return:
// Stephen Bunting won the leg with 6 shots.