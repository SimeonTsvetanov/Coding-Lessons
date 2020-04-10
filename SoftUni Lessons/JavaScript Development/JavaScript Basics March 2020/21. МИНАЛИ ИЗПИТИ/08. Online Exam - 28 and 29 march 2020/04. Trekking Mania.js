function treckingMania(input) {
    // Mask
    let groups = Number(input.shift());
    
    let total = 0;
    let mussala = 0;
    let montblanc = 0;
    let kilimandjaro = 0;
    let k2 = 0;
    let everest = 0;

    for (let group = 1; group <= groups; group += 1) {
        let count = Number(input.shift());
        total += count;

        if (count <= 5) {mussala += count;}
        else if (count >= 6 && count <= 12) {montblanc += count;}
        else if (count >= 13 && count <= 25) {kilimandjaro += count;}
        else if (count >= 26 && count <= 40) {k2 += count;}
        else if (count >= 41) {everest += count;}
    }

    console.log(`${(mussala / total * 100).toFixed(2)}%`);
    console.log(`${(montblanc / total * 100).toFixed(2)}%`);
    console.log(`${(kilimandjaro / total * 100).toFixed(2)}%`);
    console.log(`${(k2 / total * 100).toFixed(2)}%`);
    console.log(`${(everest / total * 100).toFixed(2)}%`);
}

treckingMania([10, 10, 5, 1, 100, 12, 26, 17, 37, 40, 78]);  // Should return:
// 1.84%
// 6.75%
// 5.21%
// 31.60%
// 54.60%

treckingMania([5, 25, 41, 31, 250, 6]);  // Should return:
// 0.00%
// 1.70%
// 7.08%
// 8.78%
// 82.44%
