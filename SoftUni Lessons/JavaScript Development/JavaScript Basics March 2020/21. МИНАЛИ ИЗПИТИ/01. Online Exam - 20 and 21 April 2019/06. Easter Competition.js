function easterCompetition(input) {
    // Mask
    let count = Number(input.shift());

    let bestChef = undefined;
    let bestPoints = Number.MIN_SAFE_INTEGER;

    for (let times = 1; times <= count; times += 1) {
        let chef = input.shift();
        let points = 0;
        while ('command is Stop') {
            let command = input.shift();
            if (command == "Stop") {
                console.log(`${chef} has ${points} points.`);
                if (points > bestPoints) {
                    bestChef = chef;
                    bestPoints = points;
                    console.log(`${chef} is the new number 1!`);
                }
                break;
            }
            points += Number(command);

        }
    }

    console.log(`${bestChef} won competition with ${bestPoints} points!`);
}

easterCompetition([3, 'Chef Manchev', 10, 10, 10, 10, 'Stop', 'Natalie', 8, 2, 9, 'Stop', 'George', 9, 2, 4, 2, 'Stop']); 
// Should return:
// Chef Manchev has 40 points.
// Chef Manchev is the new number 1!
// Natalie has 19 points.
// George has 17 points.
// Chef Manchev won competition with 40 points!


easterCompetition([2, 'Chef Angelov', 9, 9, 9, 'Stop', 'Chef Rowe', 10, 10, 10, 10, 'Stop']);  
// Should return:
// Chef Angelov has 27 points.
// Chef Angelov is the new number 1!
// Chef Rowe has 40 points.
// Chef Rowe is the new number 1!
// Chef Rowe won competition with 40 points!
