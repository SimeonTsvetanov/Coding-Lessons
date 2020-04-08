function easterShop(input) {
    // Mask
    let eggs = Number(input.shift());
    let sold = 0;

    while ("I say so!") {
        let buyFillClose = input.shift();
        
        if (buyFillClose == 'Close') {
            console.log(`Store is closed!`);
            console.log(`${sold} eggs sold.`)
            break;
        } else if (buyFillClose == "Fill") {
            eggs += Number(input.shift());
        } else if (buyFillClose == 'Buy') {
            let count = Number(input.shift());
            if (eggs - count < 0) {
                console.log(`Not enough eggs in store!`);
                console.log(`You can buy only ${eggs}.`);
                break;
            } else {
                eggs -= count;
                sold += count;
            }
        }
    }
}

easterShop([13, 'Buy', 8, 'Fill', 3, 'Buy', 10 ]);  // Should return:
// Not enough eggs in store!
// You can buy only 8.

easterShop([20, 'Fill', 30, 'Buy', 15, 'Buy', 20, 'Close']);  // Should return:
// Store is closed!
// 35 eggs sold.
