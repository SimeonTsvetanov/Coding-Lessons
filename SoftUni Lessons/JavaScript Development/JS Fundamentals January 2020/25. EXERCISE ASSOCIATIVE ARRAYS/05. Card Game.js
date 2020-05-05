function cardGame(input) {
    // Mask

    let players = {};
    input.forEach(data => {
        let player = data.split(': ')[0];
        let cards =  data.split(': ')[1].split(', ');
        if (players.hasOwnProperty(player)) {
            cards.forEach(card => {
                if (!players[player].includes(card)) {
                    players[player].push(card);
                }
            })
        } else {
            let newCards = [];
            cards.forEach(card => {
                if (!newCards.includes(card)) {
                    newCards.push(card);
                }
            })
            players[player] = newCards;
        }
    })

    let powers = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, J: 11, Q: 12, K: 13, A: 14};
    let types = {S: 4, H: 3, D: 2, C: 1};

    for (let [player, cards] of Object.entries(players)) {
        let total = 0;
        cards.forEach(card => {
            card = card.split('');
            let type = types[card.pop()];
            let power = powers[card.join('')];
            total += type * power;
        })
        console.log(`${player}: ${total}`);
    }
}


cardGame([
        'Pesho: 2C, 4H, 9H, AS, QS',
        'Slav: 3H, 10S, JC, KD, 5S, 10S',
        'Peshoslav: QH, QC, QS, QD',
        'Slav: 6H, 7S, KC, KD, 5S, 10C',
        'Peshoslav: QH, QC, JS, JD, JC',
        'Pesho: JD, JD, JD, JD, JD, JD'
    ]);
// Should return:
// Pesho: 167
// Slav: 175
// Peshoslav: 197

