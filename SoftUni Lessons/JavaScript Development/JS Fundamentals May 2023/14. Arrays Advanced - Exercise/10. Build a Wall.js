function buildAWall (walls) {
    // MasK
    let days = []
    let spend = 0;

    while (true) {
        if (walls.every((currentValue) => currentValue === 30)) {
            break;
        }

        let daily = 0
        for (let i = 0; i < walls.length; i++) {
            if (walls[i] < 30) {
                walls[i] += 1
                daily += 195;
            }
        }
        days.push(daily);
    }

    console.log(days.join(', '));
    console.log(`${days.reduce((a, b) => a + b, 0) * 1900} pesos`);
}

buildAWall([21, 25, 28]);