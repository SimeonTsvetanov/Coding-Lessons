function mask (params) {
    // MASK
    const n = params;

    for(let i = 1; i <= n; i++) {
        let sum = i.toString().split('').map(Number).reduce((a, b) => a + b, 0);
        let special = '';
        [5, 7, 11].includes(sum) ? special = "True" : special = "False";
        console.log(`${i} -> ${special}`);
    }
}

mask(15);
// 1 -> False
// 2 -> False
// 3 -> False
// 4 -> False
// 5 -> True
// 6 -> False
// 7 -> True
// 8 -> False
// 9 -> False
// 10 -> False
// 11 -> False
// © SoftUni – https://softuni.org. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
//
// Follow us: Page 6 of 7
// 12 -> False
// 13 -> False
// 14 -> True
// 15 -> False
