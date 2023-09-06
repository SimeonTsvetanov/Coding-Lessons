function mask (params) {
    // MASK
    let leaders = {};

    params.forEach(param => {
        if (param.includes("arrives")) {
            let leader = param.split(' ').filter(x => x !== 'arrives').join(' ');
            leaders[leader] = {};
        } else if (param.includes(": ")) {
            param = param.split(": ");
            let leader = param.shift();
            let army = param[0].split(", ")[0];
            let count = Number(param[0].split(", ")[1]);
            if (leader in leaders) { leaders[leader][army] = count; }
        } else if (param.includes("+")) {
            let army = param.split(' + ')[0];
            let count = Number(param.split(' + ')[1]);
            for (let [leader, armies] of Object.entries(leaders)) {
                for (let [c_army, c_count] of Object.entries(armies)) {
                    if (c_army === army) {
                        leaders[leader][c_army] += count;
                    }
                }
            }
        } else if (param.includes(" defeated")) {
            let leader = param.split(" defeated")[0];
            if (leader in leaders) {
                delete leaders[leader];
            }
        }
    });

    for (let [leader, armies] of Object.entries(leaders).sort((a, b) => {
        return Object.values(b[1]).reduce((a, b) => a + b, 0) - Object.values(a[1]).reduce((a, b) => a + b, 0);
    })) {
        console.log(`${leader}: ${Object.values(armies).reduce((a, b) => a + b, 0)}`);
        for (let [army, count] of Object.entries(armies).sort((a, b) => {
            return b[1] - a[1];
        })) {
            console.log(`>>> ${army} - ${count}`);
        }
    }
}

mask(['Rick Burr arrives', 'Fergus: Wexamp, 30245', 'Rick Burr: Juard, 50000', 'Findlay arrives', 'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350', 'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000', 'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']);
// Porter: 58507
// >>> Legion - 55302
// >>> Retix - 3205
// Findlay: 39040
// >>> Britox - 39040

console.log('-------------------------------------');

mask(['Rick Burr arrives',
    'Findlay arrives', 'Rick Burr: Juard, 1500',
    'Wexamp arrives', 'Findlay: Wexamp, 34540', 'Wexamp + 340', 'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423']);
//
