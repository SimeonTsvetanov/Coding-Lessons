// NOT SOLVED .... I hate the problem description it's like a little book. WTF
// Not worth my time!

function bunnyKill (data) {
    // MasK
    let coordinates = data.pop();
    let hangar = data.map(row => row.split(' ').map(Number));

    console.log(hangar);
    console.log('---------');
    console.log(coordinates);
}

bunnyKill(['5 10 15 20',
    '10 10 10 10',
    '10 15 10 10',
    '10 10 10 10',
    '2,2 0,1']
);

// 70
// 7

console.log('------------------------');
console.log('------------------------');


bunnyKill(['10 10 10',
    '10 10 10',
    '10 10 10',
    '0,0']
);

// 60
// 6
