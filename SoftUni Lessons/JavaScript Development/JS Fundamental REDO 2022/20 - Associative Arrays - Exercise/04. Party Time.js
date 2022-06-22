function partyTime(input) {
    // Mask - Solution from work in class back in 2020:

    function createList(guestArr) {
        let guests = {
            vip: [],
            regular: []
        };
        guestArr.forEach(guest => {
            if (isNaN(Number(guest[0]))) {
                guests.regular.push(guest);
            } else {
                guests.vip.push(guest);
            }
        })
        return guests;
    }

    function removeGusts(arr, guestObj) {
        arr.forEach(guest => {
            if (guestObj.vip.includes(guest)) {
                guestObj.vip.splice(guestObj.vip.indexOf(guest), 1);
            }
            if (guestObj.regular.includes(guest)) {
                guestObj.regular.splice(guestObj.regular.indexOf(guest), 1);
            }
        })
        return guestObj
    }

    function createOutput(guests) {
        // let output = [];
        // guests.vip.forEach(vip => output.push(vip));
        // guests.regular.forEach(reg => output.push(reg));
        // return output;
        let output = guests.vip.concat(guests.regular);
        return output.length + '\n' + output.join('\n');
    }

    let partyIndex = input.indexOf('PARTY');
    let guestList = createList(input.slice(0, partyIndex));
    let removedList = removeGusts(input.slice(partyIndex + 1), guestList);
    return createOutput(removedList);
}


// partyTime(['7IK9Yo0h',
//         '9NoBUajQ',
//         'Ce8vwPmE',
//         'SVQXQCbc',
//         'tSzE5t0p',
//         'PARTY',
//         '9NoBUajQ',
//         'Ce8vwPmE',
//         'SVQXQCbc'
//     ]
// );

console.log();

partyTime(['m8rfQBvl',
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
    ]
);
