function numbersNToOne(n) {
    // Mask
    while (n >= 1) {
        console.log(n);
        n--;
    }
}

numbersNToOne(5);  // Should return:
// 5
// 4
// 3
// 2
// 1

numbersNToOne(3);  // Should return:
// 3
// 2
// 1
