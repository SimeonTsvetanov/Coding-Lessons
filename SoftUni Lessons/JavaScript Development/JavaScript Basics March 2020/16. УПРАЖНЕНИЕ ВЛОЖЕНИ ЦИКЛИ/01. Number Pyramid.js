function numbersPyramid(input) {
    // Mask
    let n = Number(input.shift());
    let stop = false
    let num = 1

    for (let rows = 1; rows <= n; rows++) {
        if (stop) {break;}
        let line = ''
        for (let col = 1; col <= rows; col++) {
            line += `${num} `
            if (num == n) {stop = true; break;}
            num ++
        }
        console.log(line)
    }
}

numbersPyramid([7]);  // Should return:
// 1
// 2 3
// 4 5 6
// 7

numbersPyramid([10]);  // Should return:
// 1
// 2 3
// 4 5 6
// 7 8 9 10
