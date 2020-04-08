function easterEggsBattle(input) {
    // Mask
    let playerOne = Number(input.shift());
    let playerTwo = Number(input.shift());
    
    while ("someoneWinsORCommandToEnd") {
        let command = input.shift();    
        
        if (command == "End of battle") {
            console.log(`Player one has ${playerOne} eggs left.`);
            console.log(`Player two has ${playerTwo} eggs left.`);
            break;
        } else if (command == "one") {
            playerTwo -= 1;
            if (playerTwo == 0) {
                console.log(`Player two is out of eggs. Player one has ${playerOne} eggs left.`);        
                break;
            }
        } else if (command == "two") {
            playerOne -= 1;
            if (playerOne == 0) {
                console.log(`Player one is out of eggs. Player two has ${playerTwo} eggs left.`);
                break;
            }
        }
    }
}

easterEggsBattle([5, 4, 'one', 'two', 'one', 'two', 'two', 'End of battle']);  // Should return:
// Player one has 2 eggs left.
// Player two has 2 eggs left.

easterEggsBattle([2, 6, 'one', 'two', 'two']);  // Should return:
// Player two is out of eggs. Player one has 4 eggs left.