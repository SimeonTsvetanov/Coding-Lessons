function binaryToDecimal (...args) {
    let binary = args.shift();
    let decimal = parseInt(binary, 2);
    console.log(decimal);
}

binaryToDecimal('00001001');  // 9
binaryToDecimal(11110000);  // 240
