function logistics(input) {
    // Mask
    let cargos = Number(input.shift());

    let total = 0;
    let bus = 0;
    let truck = 0;
    let train = 0;

    for (cargo = 1; cargo <= cargos; cargo += 1) {
        let size = Number(input.shift());
        total += size;

        if (size <= 3) {
            bus += size;
        } else if (size >= 4 && size <= 11) {
            truck += size;
        } else {
            train += size;
        }
    }
    
    let average = ((bus * 200) + (truck * 175) + (train * 120)) / total;

    console.log(`${average.toFixed(2)}`)
    console.log(`${(bus / total * 100).toFixed(2)}%`)
    console.log(`${(truck / total * 100).toFixed(2)}%`)
    console.log(`${(train / total * 100).toFixed(2)}%`)
}

logistics([4, 1, 5, 16, 3]);  // Should return:
// 143.80
// 16.00%
// 20.00%
// 64.00%

logistics([5, 2, 10, 20, 1, 7]);  // Should return:
// 149.38
// 7.50%
// 42.50%
// 50.00%
