function armies (data) {
    // MasK ... the task itself is extremely simple, yet the sort is just a mess...

    let leaders = {};

    data.forEach(entry => {
        if (entry.includes(`arrives`)) {
            // We need to add new Leader:
            let newLeader = entry.split(' ').splice(0, entry.split(' ').length - 1).join(' ');
            leaders[newLeader] = {};
        } else if (entry.includes('defeated')) {
            // We need to remove a Leader:
            let leaderToRemove = entry.split(' ').splice(0, entry.split(' ').length - 1).join(' ');
            if (leaders.hasOwnProperty(leaderToRemove)) {
                delete leaders[leaderToRemove]
            }
        } else if (entry.includes(' + ')) {
            // Add count to the army:
            let armyName = entry.split(" + ")[0];
            let armyCount = +entry.split(" + ")[1];

            for (let [leader, armies] of Object.entries(leaders)) {
                if (leaders[leader].hasOwnProperty(armyName)) {
                    leaders[leader][armyName] = leaders[leader][armyName] + armyCount;
                }
            }
        } else {
            // Add the army:
            let [currentLeader, armyDetails] = entry.split(': ');
            let armyName = armyDetails.split(', ')[0];
            let armyCount = +armyDetails.split(', ')[1];
            if (leaders.hasOwnProperty(currentLeader)) {
                leaders[currentLeader][armyName] = armyCount;
            }
        }
    });

    // Not the tidies part of f***ing sorting the damn task...
    let sortedLeaders = Array.from(Object.entries(leaders)).sort((a, b) => {
        let sumA = Array.from(Object.entries(a[1])).flat().filter(x => !isNaN(x)).reduce((a, b) => a + b, 0);
        let sumB = Array.from(Object.entries(b[1])).flat().filter(x => !isNaN(x)).reduce((a, b) => a + b, 0);
        return sumB - sumA;
    })
    for (let [leader, armies] of sortedLeaders) {
        let totalPower = Array.from(Object.values(armies)).reduce((a, b) => a + b, 0);
        console.log(`${leader}: ${totalPower}`);
        let sortedArmies = Array.from(Object.entries(armies)).sort((a, b) => {
            return b[1] - a[1];
        })
        for (let [army, value] of sortedArmies) {
            console.log(`>>> ${army} - ${value}`);
        }
    }
}

armies(['Rick Burr arrives', 'Fergus: Wexamp, 30245', 'Rick Burr: Juard, 50000', 'Findlay arrives', 'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350', 'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000', 'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']);
// Porter: 58507
// >>> Legion - 55302
// >>> Retix - 3205
// Findlay: 39040
// >>> Britox - 39040
