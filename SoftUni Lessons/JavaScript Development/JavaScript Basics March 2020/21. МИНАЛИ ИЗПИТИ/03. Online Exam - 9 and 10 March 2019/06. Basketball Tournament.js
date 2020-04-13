function basketballTournament(input) {
    // Mask
    let tournamentName = undefined;
    let countGames = 0;
    let pointsOne = 0;
    let pointsTwo = 0;
    let gamesWon = 0;
    let gamesLost = 0;

    while ('I say go!') {
        tournamentName = input.shift();
        if (tournamentName == "End of tournaments") {break;}
        countGames = Number(input.shift());
        for (game = 1; game <= countGames; game +=1) {
            let pointsOne = Number(input.shift());
            let pointsTwo = Number(input.shift());
            if (pointsOne > pointsTwo) {
                console.log(`Game ${game} of tournament ${tournamentName}: win with ${pointsOne - pointsTwo} points.`);
                gamesWon += 1;
            } else {
                console.log(`Game ${game} of tournament ${tournamentName}: lost with ${pointsTwo - pointsOne} points.`);
                gamesLost += 1;
            }
        }
        
    }

    let totalGames = gamesWon + gamesLost;

    console.log(`${(gamesWon / totalGames * 100).toFixed(2)}% matches win`);
    console.log(`${(gamesLost / totalGames * 100).toFixed(2)}% matches lost`);
}


basketballTournament(['Dunkers', 2, 75, 65, 56, 73, 'Fire Girls', 3, 67, 34, 83, 98, 66, 45, 'End of tournaments']);  
// Should return:
// Game 1 of tournament Dunkers: win with 10 points.
// Game 2 of tournament Dunkers: lost with 17 points.
// Game 1 of tournament Fire Girls: win with 33 points.
// Game 2 of tournament Fire Girls: lost with 15 points.
// Game 3 of tournament Fire Girls: win with 21 points.
// 60.00% matches win
// 40.00% matches lost


basketballTournament(['Ballers', 3, 87, 63, 56, 65, 75, 64, 'Sharks', 4, 64, 76, 65, 86, 68, 99, 45, 78, 'End of tournaments ']);  
// Should return:
// Game 1 of tournament Ballers: win with 24 points.
// Game 2 of tournament Ballers: lost with 9 points.
// Game 3 of tournament Ballers: win with 11 points.
// Game 1 of tournament Sharks: lost with 12 points.
// Game 2 of tournament Sharks: lost with 21 points.
// Game 3 of tournament Sharks: lost with 31 points.
// Game 4 of tournament Sharks: lost with 33 points.
// 28.57% matches win
// 71.43% matches lost
