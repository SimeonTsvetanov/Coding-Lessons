function footballResults(params) {
    let wins = 0;
    let losses = 0;
    let drows = 0;

    for (let result of params) {
        team_one = result.split(':')[0];
        team_two = result.split(':')[1];
        
        if (team_one > team_two) {
            wins += 1;
        } else if (team_two > team_one) {
            losses += 1;
        } else {
            drows += 1;
        }
    }

    console.log(`Team won ${wins} games.`);
    console.log(`Team lost ${losses} games.`);
    console.log(`Drawn games: ${drows}`);
}


footballResults(['3:1', '0:2', '0:0']);  // Expected Result:
// Team won 1 games.
// Team lost 1 games.
// Drawn games: 1

footballResults(['4:2', '0:3', '1:0']);  // Expected Result:
// Team won 2 games.
// Team lost 1 games.
// Drawn games: 0

footballResults(['0:2', '0:1', '3:3']);  // Expected Result:
// Team won 0 games.
// Team lost 2 games.
// Drawn games: 1
