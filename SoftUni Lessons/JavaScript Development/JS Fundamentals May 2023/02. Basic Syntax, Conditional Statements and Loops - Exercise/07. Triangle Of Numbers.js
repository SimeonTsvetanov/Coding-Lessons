function mask (params) {
    // MASK
    const num = params;

    for(let i = 1; i <= num; i++) {
        let result = ''
        for (let j = 0; j < i; j++) {
            result += `${i} `;
        }
        console.log(result);
    }
}

mask(3);
// 1
// 2 2
// 3 3 3

mask(5);
// 1
// 2 2
// 3 3 3
// 4 4 4 4
// 5 5 5 5 5
