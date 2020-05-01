function heartDelivery(input) {
    // Mask
    let houses = input.shift().split('@');

    let position = 0;

    while (true) {
        let [command, jump] = input.shift().split(' ');

        if (command === 'Love!') {
            break;
        }

        position += Number(jump);
        if (position >= houses.length) {position = 0;}

        if (houses[position] <= 0) {
            console.log(`Place ${position} already had Valentine's day.`);
        } else {
            houses[position] -= 2;
            if (houses[position] <= 0) {
                console.log(`Place ${position} has Valentine's day.`);
            }
        }
    }

    console.log(`Cupid's last position was ${position}.`)
    if (houses.reduce((a, b) => a + b) === 0) {
        console.log(`Mission was successful.`);
    } else {
        console.log(`Cupid has failed ${houses.filter((a) => a > 0).length} places.`);
    }
}

heartDelivery([ '10@10@10@2', 'Jump 1', 'Jump 2', 'Love!' ]);
// Should return:
// Place 3 has Valentine's day.
// Cupid's last position was 3.
// Cupid has failed 3 places.


heartDelivery([
        '2@4@2',  'Jump 2',
        'Jump 2', 'Jump 8',
        'Jump 3', 'Jump 1',
        'Love!'
    ]);
// Should return:
// Place 2 has Valentine's day.
// Place 0 has Valentine's day.
// Place 0 already had Valentine's day.
// Place 0 already had Valentine's day.
// Cupid's last position was 1.
// Cupid has failed 1 places.
