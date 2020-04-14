function numbersMtoN(m, n) {
    // Mask
    for (let i = m; i >= n; i--) {
        console.log(i);
    }
}

numbersMtoN(6, 2);  // Should return:
// 6
// 5
// 4
// 3
// 2

numbersMtoN(4, 1);  // Should return:
// 4
// 3
// 2
// 1
