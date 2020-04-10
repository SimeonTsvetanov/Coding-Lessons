function suitcasesLoad(input) {
    // Mask
    let capacity = Number(input.shift());
    let suitcases = 0;
    let times = 0
    
    while('Command is End or no more capacity') {
        times += 1

        let command = input.shift();
        if (command == "End") {
            console.log(`Congratulations! All suitcases are loaded!`)
            break;
        }

        size = Number(command);
        if (times % 3 == 0) {size *= 1.1;} 

        if (capacity - size < 0) {
            console.log(`No more space!`)
            break;
        }

        suitcases += 1;
        capacity -= size;
    }

    console.log(`Statistic: ${suitcases} suitcases loaded.`);
}

suitcasesLoad([550, 100, 252, 72, 'End']);  // Should return:
// Congratulations! All suitcases are loaded!
// Statistic: 3 suitcases loaded.

suitcasesLoad([700.5, 180, 340.6, 126, 220]);  // Should return:
// No more space!
// Statistic: 3 suitcases loaded.
