function footballLeague(input) {
    // Mask
    let stadium_capacity = Number(input.shift());
    let count_fens = Number(input.shift());

    let a = 0;
    let b = 0;
    let v = 0;
    let g = 0;

    for (let i = 1; i <= count_fens; i++) {
        let sector = input.shift();
        
        if (sector == "A") {a += 1;}
        if (sector == "B") {b += 1;}
        if (sector == "V") {v += 1;}
        if (sector == "G") {g += 1;}
    }

    console.log(`${(a / count_fens * 100).toFixed(2)}%`);
    console.log(`${(b / count_fens * 100).toFixed(2)}%`);
    console.log(`${(v / count_fens * 100).toFixed(2)}%`);
    console.log(`${(g / count_fens * 100).toFixed(2)}%`);
    console.log(`${(count_fens / stadium_capacity * 100).toFixed(2)}%`);
}

footballLeague([1000, 12, "A", "A", "V", "V", "A", "G", "A", "A", "V", "G", "V", "A"]);  
// Should return:

// 50.00%
// 0.00%
// 33.33%
// 16.67%
// 1.20%
