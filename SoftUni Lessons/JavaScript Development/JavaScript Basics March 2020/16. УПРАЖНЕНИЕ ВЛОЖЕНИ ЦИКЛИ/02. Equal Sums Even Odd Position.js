function equalSumsEvenOddPosition(input) {
    // Mask

    let x = Number(input.shift());
    let y = Number(input.shift());
    
    let result = '';
    
    // I'll cheat a bit :D IT Rymes :D 
    for (x; x <= y; x++) {
        let z = String(x)
        let evens = Number(z[1]) + Number(z[3]) + Number(z[5]);
        let odds = Number(z[0]) + Number(z[2]) + Number(z[4]);
        if (evens == odds) {result += `${x} `;}
    }

    if (result) {console.log(result);}
}

equalSumsEvenOddPosition([100000, 100050]);  // Should return:
// 100001 100012 100023 100034 100045

equalSumsEvenOddPosition([299900, 300000]);  // Should return:
// 299970 299981 299992