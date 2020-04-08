function tennisRanklist(input) {
    // Mask
    let countChampionships = Number(input.shift());;
    let points = Number(input.shift());
    let initialPoints = points;
    let wins = 0;

    let results = {'W': 2000, 'F': 1200, 'SF': 720};

    for (let i = 1; i <= countChampionships; i += 1) {
        let result = input.shift();
        if (result == "W") {wins += 1;}
        points += results[result];
    }

    console.log(`Final points: ${points}`);
    console.log(`Average points: ${Math.floor((points - initialPoints) / countChampionships)}`);
    console.log(`${(wins / countChampionships * 100).toFixed(2)}%`);
}

tennisRanklist([5, 1400, 'F', 'SF', 'W', 'W', 'SF']);  // Should return:
// Final points: 8040
// Average points: 1328 40.00%

tennisRanklist([4, 750, 'SF', 'W', 'SF', 'W']);  // Should return:
// Final points: 6190
// Average points: 1360
// 50.00%

tennisRanklist([7, 1200, 'SF', 'F', 'W', 'F', 'W', 'SF', 'W']);  // Should return:
// Final points: 9040
// Average points: 1120
// 28.57%
