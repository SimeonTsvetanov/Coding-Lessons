function nxnMatrix(num) {
    // Mask

    // This was the lamer move:
    /*
    let matrix = [];

    for (let row = 1; row <= num; row++) {
        let rowLine = '';

        for (let col = 1; col <= num; col++) {
            rowLine += `${num} `;
        }

        matrix += `${rowLine}\n`;
    }

    console.log(matrix);
     */

    // Pro move:
    console.log(`${`${num} `.repeat(num)}\n`.repeat(num));
}

nxnMatrix(3);  // Should return:
// 3 3 3
// 3 3 3
// 3 3 3

nxnMatrix(2);  // Should return:
// 2 2
// 2 2
