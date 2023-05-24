function tennisRanklist(params) {
    let games = Number(params.shift());
    let points = Number(params.shift());

    pointsDelta = {
        "W": [2000, 0],  // [Points to Win, Count the times Won]
        "F": [1200, 0],  // [Points for Finals, Count the times on Finals]
        "SF": [720, 0]   // [Points for Semi Finals, Count the times on Semi Finals]
    }
    
    let wonPoints = 0;

    params.forEach(game => {
        wonPoints += pointsDelta[game][0];
        pointsDelta[game][1] += 1
    });

    console.log(`Final points: ${points + wonPoints}`);
    console.log(`Average points: ${Math.floor(wonPoints / params.length)}`);
    console.log(`${(pointsDelta["W"][1] / params.length * 100).toFixed(2)}%`);
}

tennisRanklist(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"]);
// Final points: 8040
// Average points: 1328 
// 40.00%

console.log('----------------------------------------------------------------');

tennisRanklist(["4",
"750",
"SF",
"W",
"SF",
"W"]);

// Final points: 6190
// Average points: 1360
// 50.00%
