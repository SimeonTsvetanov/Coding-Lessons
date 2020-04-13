function highJump(input) {
    // Mask
    let aim = Number(input.shift());
    let start = aim - 30;
    let badCount = 0;
    let totalJumps = 0;
    
    while (!(start > aim)) {
        if (badCount == 3) {break;}
        let jump = Number(input.shift());
        totalJumps += 1;
        if (jump > start) {
            start += 5;
            badCount = 0;
        } else {
            badCount += 1;
        }
    }

    if (badCount == 3) {
        console.log(`Tihomir failed at ${start}cm after ${totalJumps} jumps.`);
    } else {
        console.log(`Tihomir succeeded, he jumped over ${start - 5}cm after ${totalJumps} jumps.`)
    }
}

highJump([231, 205, 212, 213, 228, 229, 230, 235]);  // Should return:
// Tihomir succeeded, he jumped over 231cm after 7 jumps.

highJump([250, 225, 224, 225, 228, 231, 235, 234, 235]);  // Should return:
// Tihomir failed at 235cm after 8 jumps.