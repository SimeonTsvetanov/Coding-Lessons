function mask (a, del, b) {
    // MASK
    console.log(eval(`${a} ${del} ${b}`).toFixed(2));
}

mask(5,
'+',
10
);
// 15.00

mask(25.5,
'-',
3);
// 22.50
