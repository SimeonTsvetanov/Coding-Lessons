function wizardPoker(input) {
    // Mask
    let cards = input.shift().split(':');
    let deck = [];
    
    function add(card) {
        // Adds the card to the end of the deck.
        // If the card doesn't exist in print "Card not found."
        if (cards.includes(card)) {
            deck.push(card);
        }
        else { console.log('Card not found.'); }
    }

    function insert(card, index) {
        // Insert the card at the given index of the deck.
        // If the card doesn't exist or the index is invalid print "Error!"
        if (cards.includes(card) && (index >=0 && index < deck.length)) {
            deck.splice(index, 0, card);
        }
        else { console.log("Error!"); }
    }

    function remove(card) {
        // Remove the card from the deck.
        // If the card doesn't exist in print "Card not found."
        if (deck.includes(card)) {
            deck.splice(deck.indexOf(card), 1);
        }
        else { console.log("Card not found."); }
    }

    function swap(cardOne, cardTwo) {
        // Swap the positions of the cards.
        // Input will always be valid
        let indexOne = deck.indexOf(cardOne);
        let indexTwo = deck.indexOf(cardTwo);
        [deck[indexOne], deck[indexTwo]] = [deck[indexTwo], deck[indexOne]];
    }

    function shuffle() {
        // Reverse the deck
        deck.reverse();
    }
    
    function main() {
        while ('I learn JS ...(It should be a infinite loop :D)') {
            let command = input.shift().split(' ');
            if (command[0] === 'Ready') {
                break;
            }
            command[0] === 'Add' ? add(command[1]) : 'pass';
            command[0] === 'Insert' ? insert(command[1], Number(command[2])) : 'pass';
            command[0] === 'Remove' ? remove(command[1]) : 'pass';
            command[0] === 'Swap' ? swap(command[1], command[2]) : 'pass';
            command[0] === 'Shuffle' ? shuffle() : 'pass';
        }

        console.log(deck.join(' '));
    }

    main();
}

wizardPoker([
    'Innervate:Moonfire:Pounce:Claw:Wrath:Bite',
    'Add Moonfire',
    'Add Pounce',
    'Add Bite',
    'Add Wrath',
    'Insert Claw 0',
    'Swap Claw Moonfire',
    'Remove Bite',
    'Shuffle deck',
    'Ready'
]);
// Should return:
// Wrath Pounce Claw Moonfire

wizardPoker([
    'Wrath:Pounce:Lifeweaver:Exodia:Aso:Pop',
    'Add Pop',
    'Add Exodia',
    'Add Aso',
    'Remove Wrath',
    'Add SineokBqlDrakon',
    'Shuffle deck',
    'Insert Pesho 0',
    'Ready'
]);
// Should return:
// Card not found.
// Card not found.
// Error!
// Aso Exodia Pop