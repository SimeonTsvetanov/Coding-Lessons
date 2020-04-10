function passwordGenerator(input) {
    // Mask
    // You will suffer from brain crys with this task:
    let n = Number(input.shift());
    let l = Number(input.shift());

    let result = ''

    // Thats one UNGLY with CAPSLOCK madafaka :D
    for (let x1 = 1; x1 < n; x1++) {
        for (let x2 = 1; x2 < n; x2++) {
            for (let x3 = 97; x3 < (l + 97); x3++) {
                for (let x4 = 97; x4 < (l  + 97); x4++) {
                    let x = undefined;
                    if (x1 > x2) {x = x1;}
                    else {x = x2;}
                    for (let x5 = (x + 1); x5 < (n + 1); x5++) {
                        result += `${x1}${x2}${String.fromCharCode(x3)}${String.fromCharCode(x4)}${x5} `;
                    }
                }
            }
        }
    }
    console.log(result);
}

passwordGenerator([2, 4]);  // Should return:
// 11aa2 11ab2 11ac2 11ad2 11ba2 11bb2 11bc2 11bd2 11ca2 11cb2 11cc2 11cd2 11da2 11db2 11dc2 11dd2
passwordGenerator([3, 1]);  // Should return:
// 11aa2 11aa3 12aa3 21aa3 22aa3