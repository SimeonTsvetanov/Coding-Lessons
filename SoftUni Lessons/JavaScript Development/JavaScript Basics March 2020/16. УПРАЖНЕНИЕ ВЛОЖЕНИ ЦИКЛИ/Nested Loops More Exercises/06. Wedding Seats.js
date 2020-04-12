function weddingSeats(input) {
    // Mask
    // This task is ugly .. I don't like it.
    
    let lastSector = input.shift().charCodeAt(0);
    let countRowsFirstSector = Number(input.shift());
    let countSeatsOdd = Number(input.shift());

    let countSeatsEven = countSeatsOdd * 2;
    let totalSeatsSector = countSeatsOdd + countSeatsEven;
    let total = 0;

    for (let sector = 65; sector <= lastSector; sector += 1) {
        for (let j = 1; j <= countRowsFirstSector; j += 1) {
            if (j % 2 != 0) {
                for (let k = 0; k < countSeatsOdd; k += 1) {
                    console.log(`${String.fromCharCode(sector)}${j}${String.fromCharCode(k + 97)}`);
                    total += 1;
                }
            } else if (j % 2 == 0) {
                for (let k = 0; k < countSeatsOdd + 2; k += 1) {
                    console.log(`${String.fromCharCode(sector)}${j}${String.fromCharCode(k + 97)}`);
                    total += 1;
                }
            }
        }
        countRowsFirstSector += 1
    }

    console.log(total);
}

weddingSeats(['B', 3, 2]);  // Should return:
// A1a
// A1b
// A2a
// A2b
// A2c
// A2d
// A3a
// A3b
// B1a
// B1b
// B2a
// B2b
// B2c
// B2d
// B3a
// B3b
// B4a
// B4b
// B4c
// B4d
// 20

console.log() // Empty line for better readability.

weddingSeats(['C', 4, 2]);  // Should return:
// A1a
// A1b
// A2a
// A2b
// A2c
// A2d
// A3a
// A3b
// A4a
// A4b
// A4c
// A4d
// B1a
// B1b
// B2a
// B2b
// B2c
// B2d
// B3a
// B3b
// B4a
// B4b
// B4c
// B4d
// B5a
// B5b
// C1a
// C1b
// C2a
// C2b
// C2c
// C2d
// C3a
// C3b
// C4a
// C4b
// C4c
// C4d
// C5a
// C5b
// C6a
// C6b
// C6c
// C6d
// 44
