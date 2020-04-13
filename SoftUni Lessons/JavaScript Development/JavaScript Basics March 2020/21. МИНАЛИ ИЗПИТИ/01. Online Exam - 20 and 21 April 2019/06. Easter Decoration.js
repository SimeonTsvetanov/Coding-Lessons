function easterDecoration(input) {
    // Mask
    let clients = Number(input.shift());
    
    let prices = {'basket': 1.50, 'wreath': 3.80, 'chocolate bunny': 7};
    let total = 0;
    
    for (let client = 1; client <= clients; client += 1) {
        let count = 0;
        let price = 0;
        while('commmand is Finish') {
            let product = input.shift();
            if (product == "Finish") {
                // TODO
                if (count % 2 == 0) {price *= 0.8;}
                total += price;
                console.log(`You purchased ${count} items for ${price.toFixed(2)} leva.`);
                break;
            }
            price += prices[product];
            count += 1;
        }
    }

    console.log(`Average bill per client is: ${(total / clients).toFixed(2)} leva.`);
}

easterDecoration([2, 'basket', 'wreath', 'chocolate bunny', 'Finish', 'wreath', 'chocolate bunny', 'Finish']);  
// Should return:
// You purchased 3 items for 12.30 leva.
// You purchased 2 items for 8.64 leva.
// Average bill per client is: 10.47 leva.


easterDecoration([1, 'basket', 'wreath', 'chocolate bunny', 'wreath', 'basket', 'chocolate bunny', 'Finish']);  
// Should return:
// You purchased 6 items for 19.68 leva.
// Average bill per client is: 19.68 leva.
