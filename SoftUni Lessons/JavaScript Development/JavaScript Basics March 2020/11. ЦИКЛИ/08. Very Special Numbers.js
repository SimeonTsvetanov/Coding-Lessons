function verySpecialNumer(startt, endd, nn) {
    // Mask
    let start = Number(startt);
    let end = Number(endd);
    let n = Number(nn);
    for (start; start <= end; start +=1) {
        if ((start % (n * n) == 0) && (start % n == 0)) {
            console.log(`Very special number: ${start}`);
        } else if (start % n == 0) {
            console.log(`Special number: ${start}`);
        } else {
            console.log(start);
        }
    }
}

verySpecialNumer(1, 25, 3);  // Should return:
// 1
// 2
// Special number: 3
// 4
// 5
// Special number: 6
// 7
// 8
// Very special number: 9
// 10
// …
// Special number: 21
// 22
// 23
// Special number: 24
// 25

verySpecialNumer(1, 10, 4);  // Should return:
// 1
// 2
// 3
// Special number: 4
// 5
// 6
// 7
// Special number: 8
// 9
// 10
