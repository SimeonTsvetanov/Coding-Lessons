function triplesOfLatinLetters(num) {
    // Mask
    let firstNum = 'a'.charCodeAt(0);

    for (let i = 0; i < num; i += 1) {
        for (let j = 0; j  < num; j += 1) {
            for (let k = 0; k < num; k += 1) {
                console.log(String.fromCharCode(
                    firstNum + i,
                    firstNum + j,
                    firstNum + k));
            }
        }
    }
}

triplesOfLatinLetters(3);  // Should return:
// aaa
// aab
// aac
// aba
// abb
// abc
// aca
// acb
// acc
// baa
// bab
// bac
// bba
// bbb
// bbc
// bca
// bcb
// bcc
// caa
// cab
// cac
// cba
// cbb
// cbc
// cca
// ccb
// ccc
