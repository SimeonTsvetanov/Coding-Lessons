function trekkingMania(params) {
    let groups = {
        0: [],  // <= 5 Mussala
        1: [],  // 6 … 12 Mont Blanc
        2: [],  // 13 … 25 Kalimanjaro
        3: [],  // 26 … 40 K2
        4: [],  // ≥ 41 Everest
    }
    let groupsCount = Number(params.shift());

    let allGroups = params.map(Number);
    let totalPeople = allGroups.reduce((a, b) => a + b, 0);


    allGroups.forEach(num => {
        if (num <= 5) {
            groups[0].push(num);
        } else if (num >= 6 && num <= 12) {
            groups[1].push(num);
        } else if (num >= 13 && num <= 25) {
            groups[2].push(num);
        } else if (num >= 26 && num <= 40) {
            groups[3].push(num);
        } else {
            groups[4].push(num);
        }
    });

    for (let i = 0; i < 5; i++) {
        console.log(`${(groups[i].reduce((a, b) => a + b, 0) / totalPeople * 100).toFixed(2)}%`);
    }
}

trekkingMania(["10",
"10",
"5",
"1",
"100",
"12",
"26",
"17",
"37",
"40",
"78"]);

