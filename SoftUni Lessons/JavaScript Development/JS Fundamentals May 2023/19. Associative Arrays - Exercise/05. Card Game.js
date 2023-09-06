function mask (params) {
    // MASK
    let p = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 };
    let t = {'S': 4, 'H': 3, 'D': 2, 'C': 1};

    let players = {};

    params.forEach(param => {
        let name = param.split(': ')[0];
        let cards = param.split(': ')[1].split(', ');

        if (!(name in players)) { players[name] = []; }
        players[name] = players[name].concat(cards);
    });

    for (let [player, cards] of Object.entries(players)) {
        let filteredCards = cards.filter((a, b) => cards.indexOf(a) === b)

        let points = 0;
        filteredCards.forEach(card => {
            card = card.split('');
            points += t[card.pop()] * p[card.join('')]
        });

        console.log(`${player}: ${points}`);
    }
}

mask([
'Peter: 2C, 4H, 9H, AS, QS',
'Tomas: 3H, 10S, JC, KD, 5S, 10S',
'Andrea: QH, QC, QS, QD',
'Tomas: 6H, 7S, KC, KD, 5S, 10C',
'Andrea: QH, QC, JS, JD, JC',
'Peter: JD, JD, JD, JD, JD, JD'
]);
// Peter: 167
// Tomas: 175
// Andrea: 197

console.log('-------------------------------------');

mask([
'John: 2C, 4H, 9H, AS, QS',
'Slav: 3H, 10S, JC, KD, 5S, 10S',
'Alex: 6H, 7S, KC, KD, 5S, 10C',
'Thomas: QH, QC, JS, JD, JC',
'Slav: 6H, 7S, KC, KD, 5S, 10C',
'Thomas: QH, QC, JS, JD, JC',
'Alex: 6H, 7S, KC, KD, 5S, 10C',
'Thomas: QH, QC, JS, JD, JC',
'John: JD, JD, JD, JD'
]);
// John: 167
// Slav: 175
// Alex: 115
// Thomas: 125
