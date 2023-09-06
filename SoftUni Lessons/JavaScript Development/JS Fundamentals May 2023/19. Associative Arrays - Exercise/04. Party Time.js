function mask (params) {
    // MASK
    let vip = [];
    let normal = [];

    while (true) {
        let guest = params.shift();
        if (guest === 'PARTY') { break; }
        if (Number(guest[0])) { vip.push(guest); } else { normal.push(guest); }
    }

    params.forEach(guest => {
        if (Number(guest[0])) {
            if (vip.includes(guest)) { vip.splice(vip.indexOf(guest), 1); }
        } else {
            if (normal.includes(guest)) { normal.splice(normal.indexOf(guest), 1); }
        }
    });

    console.log(vip.length + normal.length);
    vip.forEach(guest => { console.log(guest); });
    normal.forEach(guest => { console.log(guest); });
}

mask(['7IK9Yo0h',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc',
'tSzE5t0p',
'PARTY',
'9NoBUajQ',
'Ce8vwPmE',
'SVQXQCbc'
]
);
// 2
// 7IK9Yo0h
// tSzE5t0p

console.log('-------------------------------------');

mask(['m8rfQBvl',
'fc1oZCE0',
'UgffRkOn',
'7ugX7bm0',
'9CQBGUeJ',
'2FQZT3uC',
'dziNz78I',
'mdSGyQCJ',
'LjcVpmDL',
'fPXNHpm1',
'HTTbwRmM',
'B5yTkMQi',
'8N0FThqG',
'xys2FYzn',
'MDzcM9ZK',
'PARTY',
'2FQZT3uC',
'dziNz78I',
'mdSGyQCJ',
'LjcVpmDL',
'fPXNHpm1',
'HTTbwRmM',
'B5yTkMQi',
'8N0FThqG',
'm8rfQBvl',
'fc1oZCE0',
'UgffRkOn',
'7ugX7bm0',
'9CQBGUeJ'
]);
// 2
// xys2FYzn
// MDzcM9ZK
