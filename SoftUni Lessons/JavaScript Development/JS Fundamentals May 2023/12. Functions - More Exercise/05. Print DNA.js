function mask (number) {
    // MASK
    let str = "ATCGTTAGGG";
    let counter = 0;
    for (let i = 0; i < number; i++) {
        if (i % 4 == 0) {
            console.log(`**${str[counter % 10]}${str[(counter % 10) + 1]}**`);
        } else if (i % 4 == 1) {
            console.log(`*${str[counter % 10]}--${str[(counter % 10) + 1]}*`);
        } else if (i % 4 == 2) {
            console.log(`${str[counter % 10]}----${str[(counter % 10) + 1]}`);
        } else if (i % 4 == 3) {
            console.log(`*${str[counter % 10]}--${str[(counter % 10) + 1]}*`);
        }
        counter += 2;
    }
}


mask(4);
// **AT**
// *C--G*
// T----T
// *A--G*

console.log('-------------------------------------');

mask(10);
// **AT**
// *C--G*
// T----T
// *A--G*
// **GG**
// *A--T*
// C----G
// *T--T*
// **AG**
// *G--G*
