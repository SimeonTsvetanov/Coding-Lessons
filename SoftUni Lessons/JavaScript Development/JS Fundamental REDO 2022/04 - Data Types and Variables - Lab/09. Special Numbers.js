function specialNumbers (...args) {
    // MasK
    for (let n = 1; n <= args[0]; n++) {
        let special = [5, 7, 11].includes(n.toString().split('').map(Number).reduce((a, b) => a + b, 0));
        special ? console.log(`${n} -> True`) : console.log(`${n} -> False`);
    }
}

specialNumbers(9);
