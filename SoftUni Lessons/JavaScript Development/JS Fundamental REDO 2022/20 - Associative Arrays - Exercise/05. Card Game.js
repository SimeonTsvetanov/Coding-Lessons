function cardGame (data) {
    // MasK
    let people = {};

    data.forEach(entry => {
        let name = entry.split(': ')[0]
        let cards = entry.split(': ')[1].split(', ');
        people.hasOwnProperty(name) ? people[name] = people[name].concat(cards) : people[name] = cards;
    });

    let powers = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    let types = {
        'S': 4, 'H': 3, 'D': 2, 'C': 1
    }

    for (const [name, cards] of Object.entries(people)) {
        let powerScore = 0;
        let typeScore = 0;
        let score = 0;
        const uniqueCards = [...new Set(cards)];
        uniqueCards.forEach(card => {
            card = card.split('');
            let type = card.pop();
            let power = card.join('');
            score += powers[power] * types[type];
        });
        console.log(`${name}: ${score}`);
    }
}

cardGame([
        'Peter: 2C, 4H, 9H, AS, QS',
        'Tomas: 3H, 10S, JC, KD, 5S, 10S',
        'Andrea: QH, QC, QS, QD',
        'Tomas: 6H, 7S, KC, KD, 5S, 10C',
        'Andrea: QH, QC, JS, JD, JC',
        'Peter: JD, JD, JD, JD, JD, JD'
    ]
);

// Peter: 167
// Tomas: 175
// Andrea: 197

console.log();

cardGame([
        'John: 2C, 4H, 9H, AS, QS',
        'Slav: 3H, 10S, JC, KD, 5S, 10S',
        'Alex: 6H, 7S, KC, KD, 5S, 10C',
        'Thomas: QH, QC, JS, JD, JC',
        'Slav: 6H, 7S, KC, KD, 5S, 10C',
        'Thomas: QH, QC, JS, JD, JC',
        'Alex: 6H, 7S, KC, KD, 5S, 10C',
        'Thomas: QH, QC, JS, JD, JC',
        'John: JD, JD, JD, JD'
    ]
);

// John: 167
// Slav: 175
// Alex: 115
// Thomas: 125
