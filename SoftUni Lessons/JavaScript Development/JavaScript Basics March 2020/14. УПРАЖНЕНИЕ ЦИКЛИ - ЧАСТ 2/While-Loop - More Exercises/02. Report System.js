function reportSystem(params) {
    let aim = Number(params.shift());

    let timesCash = 0;
    let totalCash = 0;

    let timesCard = 0;
    let totalCard = 0;

    let times = 1;
    while ("We colect the money or they say End") {
        let product = params.shift();
        
        if (product == 'End') {
            console.log(`Failed to collect required money for charity.`);
            break;
        }
        
        product = Number(product);
        
        if (times % 2 != 0) {
            // We get paid in cash.
            if (product > 100) {
                console.log(`Error in transaction!`);
            } else {
                aim -= product;
                console.log(`Product sold!`)
                timesCash += 1;
                totalCash += product
            }

        } else {
            // We get paid with card.
            if (product < 10) {
                console.log(`Error in transaction!`);
            } else {
                aim -= product;
                console.log(`Product sold!`)
                timesCard += 1
                totalCard += product
            }
        }

        times += 1;

        if (aim <= 0) {
            console.log(`Average CS: ${(totalCash / timesCash).toFixed(2)}`);
            console.log(`Average CC: ${(totalCard/ timesCard).toFixed(2)}`);
            break;
        }
    }
}

reportSystem([500, 120, 8, 63, 256, 78, 317]);  // Expected Output:
// Error in transaction!
// Error in transaction!
// Product sold!
// Product sold!
// Product sold!
// Product sold!
// Average CS: 70.50
// Average CC: 286.50

reportSystem([600, 86, 150, 98, 227, 'End']);  // Expected Output:
// Product sold!
// Product sold!
// Product sold!
// Product sold!
// Failed to collect required money for charity.
