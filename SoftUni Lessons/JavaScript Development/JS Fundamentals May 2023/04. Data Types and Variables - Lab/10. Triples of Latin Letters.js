function mask (params) {
    // MASK
    let n = params;

    for(let a = 0; a < n; a++) {
        for(let b = 0; b < n; b++) {
            for(let c = 0; c < n; c++) {

                let first = String.fromCharCode(97 + a);
                let second = String.fromCharCode(97 + b);
                let third = String.fromCharCode(97 + c);

                console.log(`${first}${second}${third}`);
            }
        }
    }
}

mask(3);
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

mask(2);
// aaa
// aab
// aba
// abb
// baa
// bab
// bba
// bbb
