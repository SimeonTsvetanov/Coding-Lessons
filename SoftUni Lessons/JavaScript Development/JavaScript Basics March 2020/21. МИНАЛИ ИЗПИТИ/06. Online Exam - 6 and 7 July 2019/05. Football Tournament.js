function footballTournalment(input) {
    // Mask
    let name = input.shift();
    let games = Number(input.shift());

    if (games == 0) {
        console.log(`${name} hasn't played any games during this season.`);
        return
    }

    let points = {
        // How it works
        // "W/D/L": [points won, times]
        // And in the Total we keep the total points :)
        "W": [3, 0],
        "D": [1, 0],
        "L": [0, 0],
        "Total": 0
    };

    for (let game = 1; game <= games; game += 1) {
        let score = input.shift();
        points[score][1] += 1;  // We add the stat how many times we have W/D/L
        points["Total"] += points[score][0];  // We are adding the points won.
    }

    console.log(`${name} has won ${points['Total']} points during this season.`);
    console.log(`Total stats:`);
    console.log(`## W: ${points["W"][1]}`);
    console.log(`## D: ${points["D"][1]}`);
    console.log(`## L: ${points["L"][1]}`);
    console.log(`Win rate: ${(points["W"][1] / games * 100).toFixed(2)}%`);
}

footballTournalment(['Liverpool', 10, 'W', 'D', 'D', 'W', 'L', 'W', 'D', 'D', 'W', 'W']);  
// Should return:
// Liverpool has won 19 points during this season.
// Total stats:
// ## W: 5
// ## D: 4
// ## L: 1
// Win rate: 50.00%

footballTournalment(['Chelsea', 0]);  // Should return:
// Chelsea hasn't played any games during this season.