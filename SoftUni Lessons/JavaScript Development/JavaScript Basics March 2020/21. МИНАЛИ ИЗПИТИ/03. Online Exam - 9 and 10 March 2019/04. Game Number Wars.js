function gameNumberWars(input) {
    // Mask
    let playerOne = input.shift();
    let playerTwo = input.shift();

    let playerOnePoints = 0;
    let playerTwoPoints = 0;

    while ('I have farts!') {
        let command = input.shift();
        if (command == 'End of game') {
            console.log(`${playerOne} has ${playerOnePoints} points`)
            console.log(`${playerTwo} has ${playerTwoPoints} points`)
            break;  // And stop the Program.
        }

        let playerOneCard = Number(command);
        let playerTwoCard = Number(input.shift());

        if (playerOneCard > playerTwoCard) {playerOnePoints += playerOneCard - playerTwoCard;}
        else if (playerTwoCard > playerOneCard) {playerTwoPoints += playerTwoCard - playerOneCard;}
        else {
            // We have Number Wars.... 
            console.log("Number wars!");
            let finalPlayerOneCard = Number(input.shift());
            let finalPlayerTwoCard = Number(input.shift());

            if (finalPlayerOneCard > finalPlayerTwoCard) {
                console.log(`${playerOne} is winner with ${playerOnePoints} points`);
            } else {
                console.log(`${playerTwo} is winner with ${playerTwoPoints} points`);
            }
            break;  // And stop the Program.
        }
    }
}

gameNumberWars(['Desi', 'Niki', 7, 5, 3, 4, 3, 3, 5, 3]);  // Should return:
// Number wars!
// Desi is winner with 2 points

gameNumberWars(['Elena', 'Simeon', 6, 3, 2, 5, 8, 9, 'End of game']);  // Should return:
// Elena has 3 points
// Simeon has 4 points
