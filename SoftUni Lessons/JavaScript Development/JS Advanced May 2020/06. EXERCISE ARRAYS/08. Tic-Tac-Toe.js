// Not included in final score
function ticTacToe(commands = []) {
    // Mask
    function checkForWinner() {
        let winner = false;
        for (let i = 0; i < 3; i ++) {
            // Horizontal:
            if (new Set(board[i]).size === 1 && !(board[i].includes('false'))) {
                winner = board[i][i]
                return winner;
            }
            // Vertical:
            let vertical = [board[0][i], board[1][i], board[2][i]];
            if (new Set(vertical).size === 1 && !(vertical.includes('false'))) {
                winner = board[i][0]
                return winner;
            }
            // Diagonals: ... yeah, yeah not optimized. Just take it out of the loop. Snob!
            let left = [board[0][0], board[1][1], board[2][2]];
            let right = [board[0][2], board[1][1], board[2][0]];
            if ((new Set(left).size === 1 || new Set(right).size === 1) && board[1][1] === 'O') {winner = 'O'; return winner}
            if ((new Set(left).size === 1 || new Set(right).size === 1) && board[1][1] === 'X') {winner = 'X'; return winner}
        }
        return winner
    }

    // Ill do false's in strings as its easier for me.
    let board = [
            ['false', 'false', 'false'],
            ['false', 'false', 'false'],
            ['false', 'false', 'false']]

    let player = 'X';  // The first Player is X...

    for (let move of commands) {
        // Main Loop:
        move = move.split(' ').map(Number);

        // Check if the space is taken:
        if (board[move[0]][move[1]] !== 'false') {
            console.log(`This place is already taken. Please choose another!`);
            continue
        }

        // Place the Move:
        board[move[0]][move[1]] = player;

        // Change the player:
        player === 'X' ? player = "O" : player = 'X';

        // Check to Win:
        let winner = checkForWinner();
        if (winner) {
            console.log(`Player ${winner} wins!`);
            break;  // End the main loop
        }

        // Check For Tie:
        if (!(board.flat().includes('false'))) {
            console.log('The game ended! Nobody wins :(');
            break;  // End the main loop
        }
    }

    // Print the board in the ugliest way possible...
    for (let row of board) {
        console.log(row.join('\t'))
    }
}

ticTacToe([
    "0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 1",
    "1 2",
    "2 2",
    "2 1",
    "0 0"]
);  // Should return:
// Player O wins!
//     O	X	X
// X	O	X
// O	false	O

ticTacToe(["0 0",
    "0 0",
    "1 1",
    "0 1",
    "1 2",
    "0 2",
    "2 2",
    "1 2",
    "2 2",
    "2 1"]
);  // Should return:
// This place is already taken. Please choose another!
//     Player X wins!
//     X	X	X
// false	O	O
// false	false	false

ticTacToe(["0 1",
    "0 0",
    "0 2",
    "2 0",
    "1 0",
    "1 2",
    "1 1",
    "2 1",
    "2 2",
    "0 0"
]);  // Should Return:
// The game ended! Nobody wins :(
// O	X	X
// X	X	O
// O	O  	X
